#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TSystem.h"

#include "TLorentzVector.h"
#include "TMath.h"

#include <string>

class fakeparent : public multidraw::TTreeFunction {
public:
  fakeparent(const char* type_);

  char const* getName() const override { return "fakeparent"; }
  TTreeFunction* clone() const override { return new fakeparent(ParentType.c_str()); }
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  int getXLepton();
  std::string ParentType;

  UIntValueReader*  nLepton;
  FloatArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;
  FloatArrayReader* Lepton_phi;
  IntArrayReader*   Lepton_pdgId;
  IntArrayReader*   Lepton_electronIdx;
  IntArrayReader*   Lepton_muonIdx;
  IntArrayReader*   Electron_genPartIdx;
  IntArrayReader*   Muon_genPartIdx;
  IntArrayReader*   GenPart_pdgId;
  IntArrayReader*   GenPart_genPartIdxMother;
  IntArrayReader*   GenPart_statusFlags;
};

fakeparent::fakeparent(const char* type_) :
  TTreeFunction(),
  ParentType{type_}
{}

double
fakeparent::evaluate(unsigned)
{
  int iL = getXLepton();
  if (iL == -1) return -1.0;
  int genLepIdx = -1;
  if (Lepton_electronIdx->At(iL) >= 0) genLepIdx = Electron_genPartIdx->At((unsigned)Lepton_electronIdx->At(iL));
  if (Lepton_muonIdx->At(iL) >= 0) genLepIdx = Muon_genPartIdx->At((unsigned)Lepton_muonIdx->At(iL));
  if (genLepIdx == -1) return -1.0;
  int motherIdx = genLepIdx;
  while (motherIdx >= 0 && GenPart_pdgId->At((unsigned)genLepIdx) == GenPart_pdgId->At((unsigned)motherIdx)){
    motherIdx = GenPart_genPartIdxMother->At((unsigned)motherIdx);
  }
  int firstMotherIdx = motherIdx;
  if (ParentType == "prompt"){
    while (motherIdx >= 0 && (GenPart_statusFlags->At((unsigned)motherIdx)&1)!=1) motherIdx = GenPart_genPartIdxMother->At((unsigned)motherIdx);
  }
  if (ParentType == "hard"){
    while (motherIdx >= 0 && (GenPart_statusFlags->At((unsigned)motherIdx)&128)!=128) motherIdx = GenPart_genPartIdxMother->At((unsigned)motherIdx);
  }
  double motherId = motherIdx < 0 ? -1.0 : (double)TMath::Abs(GenPart_pdgId->At(motherIdx));
  return motherId;
}

int
fakeparent::getXLepton(){
  unsigned nLep{*nLepton->Get()};
  if (nLep<3) return -1;
  int XLepton = -1;
  float minmllDiffToZ = 9999.0;
  for (int iL = 0; iL < 2; iL++){
    for (int jL = iL+1; jL < 3; jL++){
      if (Lepton_pdgId->At(iL) + Lepton_pdgId->At(jL) == 0){
	TLorentzVector iLep;
	TLorentzVector jLep;
	iLep.SetPtEtaPhiM(Lepton_pt->At(iL),Lepton_eta->At(iL),Lepton_phi->At(iL),0.0);
	jLep.SetPtEtaPhiM(Lepton_pt->At(jL),Lepton_eta->At(jL),Lepton_phi->At(jL),0.0);
	float mllDiffToZ = TMath::Abs((iLep+jLep).M()-91.1876);
	if (mllDiffToZ < minmllDiffToZ){
	  XLepton = 3-iL-jL;
	  minmllDiffToZ = mllDiffToZ;
	}
      }
    }
  } 
  return XLepton;
}  

void
fakeparent::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton,                  "nLepton");
  _library.bindBranch(Lepton_pt,                "Lepton_pt");
  _library.bindBranch(Lepton_eta,               "Lepton_eta");
  _library.bindBranch(Lepton_phi,               "Lepton_phi");
  _library.bindBranch(Lepton_pdgId,             "Lepton_pdgId");
  _library.bindBranch(Lepton_electronIdx,       "Lepton_electronIdx");
  _library.bindBranch(Lepton_muonIdx,           "Lepton_muonIdx");
  _library.bindBranch(Electron_genPartIdx,      "Electron_genPartIdx");
  _library.bindBranch(Muon_genPartIdx,          "Muon_genPartIdx");
  _library.bindBranch(GenPart_pdgId,            "GenPart_pdgId");
  _library.bindBranch(GenPart_genPartIdxMother, "GenPart_genPartIdxMother");
  _library.bindBranch(GenPart_statusFlags,      "GenPart_statusFlags");
}
