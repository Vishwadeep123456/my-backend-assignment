from pydantic import BaseModel

# ----- Bogie Checksheet -----
class BMBCChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: str
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

class BogieChecksheetForm(BaseModel):
    bmbcChecksheet: BMBCChecksheet
    bogieChecksheet: BogieChecksheet
    bogieDetails: BogieDetails
    formNumber: str
    inspectionBy: str
    inspectionDate: str

# ----- Wheel Specification -----
class WheelFields(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile: str

class WheelSpecificationForm(BaseModel):
    fields: WheelFields
    formNumber: str
    submittedBy: str
    submittedDate: str

