import google.generativeai as genai

genai.configure(api_key="ENTER_YOUR_API")
model = genai.GenerativeModel("gemini-1.5-flash")

NER = """

Do Named Entity Relationship for below in JSON in detail where equipment is main object

TECHNICAL  SPECIFICATIONS (TS) OF HSC PUMP 
FOR 
 Composite work of Manufacture & Supply, Erection, Commissioning and Testing at 
site of 14 Nos. H.S.C. Centrifugal Pumps, 60 Cusec capacity and 37.0 Meter Head 
along with suitable 14 Nos. 11 KV HT Squirrel Cage Induction Motor, suitable 14 
Nos. 11 KV HT Capacitor, Suitable 02 Sets of (11 KV, 3-Phase HT Switchgear Panel 
(VCB Type) consisting of 02 Nos. Incoming Panel, 14 Nos. Outgoing Motor Feeder 
Panel, 01 No & 01 No. Bus Coupler for Each Stage, all connected with common bus-
bar arrangement and compatible with latest technology of automation for 
monitoring through SCADA, 14 Nos. C.I. Butterfly Valve 750 mm dia, 14 Nos. C.I. 
Sluice Valve 750 mm dia and 14 Nos. C.S. Reflux Valve 750 mm dia in the Pucca 
Pump House of Yamuna Pump Canal Stage-Ist, District-Prayagraj under jurisdiction 
of Lift Irrigation Division, Prayagraj, Irrigation Department, U.P. 
 
 
1.00 SCOPE 
 This tender/Bid is for the issue of contract for Composite work of Manufacture & 
Supply, Erection, Commissioning and Testing at site of 10 Nos. H.S.C. Centrifugal 
Pumps, 60 Cusec capacity and 37.0 Meter Head along with suitable 10 Nos. 11 KV 
HT Squirrel Cage Induction Motor, suitable 10 Nos. 11 KV HT Capacitor, Suitable 01 
Sets of (11 KV, 3-Phase HT Switchgear Panel (VCB Type) consisting of 02 Nos. 
Incoming Panel, 10 Nos. Outgoing Motor Feeder Panel, 01 No. Transformer Feeder 
Panel (Indoor, draw-out Type) & 01 No. Bus Coupler) Panel, all connected with 
common bus-bar arrangement and compatible with latest technology of automation 
for monitoring through SCADA, 10 Nos. C.I. Butterfly Valve 750 mm dia, 10 Nos. C.I. 
Sluice Valve 750 mm dia and 10 Nos. C.S. Reflux Valve 750 mm dia in the Pucca 
Pump House of Yamuna Pump Canal Stage-Ist, District-Prayagraj under jurisdiction 
of Lift Irrigation Division, Prayagraj, Irrigation Department, U.P. as per Technical 
Specifications, Technical Conditions and relevant Indian Standards with latest 
amendments if any, stipulated in the bid documents. 
Switch Gear Panel Should be compatible with LSGI Protection to Modbus 
Protocol and should be Accompanied with Multifunction Relays and Multifunction 
meter.  
The scope of work also includes erection, commissioning and testing of aforesaid 
equipment in the Pucca Pump House on the foundation provided to enhance the 
capacity of pump canal along with already installed existing HSC Centrifugal 
Pumps having discharge capacity of 60 Cusec . Any accessories not mentioned in 
this document and deemed necessary for erection and commissioning of the 
equipment shall be in the scope of Contractor.  
The connections of newly supplied equipment with VCB Panels and other 
connections lie in the scope of Contractor.  
The Capacitors should be compatible with the motor to improve the power factor 
upto 0.96. The connections of newly supplied equipments with Panels lie in the scope 
of Contractor/ Firm.   
Necessary provisions should be provided on all equipment and accessories 
except all types of valves to ensure their compatibility for automation through SCADA. 
All types of Valves shall not be the part of Automation. All H.S.C. Pumps, HT Motors 
and their allied equipment shall have suitable slots and ports to ensure their 
connectivity with PLCs and other devices to transfer data through it. Relays should 
be RS 485 compatible to transfer signals through SCADA. Connectors with RS 485 
specifications  should be provided in the Panels to connect PLCs. 
 
2.00  GENERAL INFORMATION 
2.10   LOCATION  
Stage-Ist Stage-IInd 
The equipments shall be installed in 
Pucca Pump House at the right bank of The equipments shall be installed in 
Pucca Pump House at Bhodi Village, Yamuna river in Padua Pratappur 
Village, Tehsil Bara, District Prayagraj 
for Yamuna Pump Canal (Stage-Ist). Tehsil Bara, District Prayagraj for 
Yamuna Pump Canal (Stage-IInd). 
 
2.20    APPLICATION  
The pumps are required to run continuously round the year to lift raw 
water of Yamuna river having sand/mud content.   
 
2.30 ENVIRONMENTAL CONDITION 
2.31 AMBIENT TEMPERATURE  
 (a) Maximum : 500C 
 (b) Minimum                          : 10C 
 
2.32 HUMIDITY  
 (a) Maximum          : 80% 
 (b) Minimum                  : 25% 
2.33 QUALITY OF WATER TO BE LIFTED 
 
QUALITY OF WATER  Stage-Ist  Stage-IInd  
(a) Turbidity 1350 PPM (Silica gel) 400 PPM (Silica gel) 
(b) chlorides 48 PPM 48 PPM 
(c) Total solids 820 PPM 820 PPM 
(d) Suspended 420 PPM 420 PPM 
(e) Dissolved 400 PPM 400 PPM 
(f) Specific gravity 1.00 1.00 
(g)` Ph vaule 8.2 8.2                           
However total solids may go up to 6000 ppm during raining season. 
 
2.34 IMPORTANT R.L.’S AT SITE 
 
 IMPORTANT R.L.’S AT STAGE-I IMPORTANT R.L.’S AT STAGE-II 
(i) Altitude above sea level   – 73.36M Altitude above sea level   – 95.600M 
(ii) Lowest water level of the river-73.36M Lowest Water level in Feeder Canal  -97.770M 
(iii) Highest flood level of the river-90.370M Highest water level in feeder Canal  -98.970M 
(iv) FSL open channel (Delivery pipe)-
106.9M FSL of Canal -127.350M 
(v) Centerline of protruding piece-74.14M 
(Suction/Delivery) Centerline of protruding piece-96.702M 
(Suction/Delivery) 
(vi) Center line of Pump  -74.928M Center line of pump -97.382M 
(vii) Normal Level during running (for NPSH a 
calculation) – 72.00M Normal Level during running (for NPSH a 
calculation) – 93.922M 
 
2.35 SUCTION AND DELIVERY DIA. OF PROTRUDED PIECE EMBEDED IN THE 
 WALLS 
(i) Dia. of suction side               : 750 mm 
(ii)  Dia. of delivery side                         : 900 mm 
2.36 LENGTH / DIA OF DELIVERY PIPE     : 163m/914mm  
2.37 Sluice Valve in suction side and Reflex Valve & Butterfly Valve in delivery side 
of the pump set will be provided. Sizes of the Valves will be as per pump’s 
suction/delivery sizes.  
3.00 DRAWINGS   
 Pump House dimensional drawing with foundation details and other relevant RLs of 
Yamuna Pump Canal (Stage-Ist and Stage-IInd) can be obtain on demand from the 
office as mentioned in NIT in any working day and time. 
(1) General arrangement drawing of Pump installed in Pump House (Stage-Ist & 
Stage-IInd) 
(2) Layout Diagram of Panel (Stage-Ist and Stage-IInd) 
 4.00 STANDARDS 
The equipments shall conform to the following Indian Standards Specifications with 
their latest amendments if any and other relevant Indian Standards.  
 
 
Sl. No. Name of Item Standard 
1. Horizontal Split Casing Centrifugal 
Pumps IS:5120:1977; IS:6595 (Part-I)-2002, 
IS:9137:1978 IS:1520:1980 or latest if any 
2. HT Motor 11KV  /  For polarization index  IS:325:1996 /  IS:7816:1975 or latest if 
any 
3. HT Capacitors, 11KV IS:13925(Part-1):1998 or latest if any 
4. HT Switch Gear Panel (VCB Type), 11KV IS 13118:1991 / IEC: 62271 or latest if any 
5. Impeller IS: 11723(Part I):1992 or latest if any 
6. Connectors RS 485 
 
 
 
 
5.00 PUMP 
 
5.10 QUANTITY    14 Nos. 
  5.20 CONSTRUCTIONAL REQUIREMENT  
 Type of pump  Horizontal Split Casing Centrifugal 
Pump 
 No. of stages    Single  
 No. of suction inlet   Double suction 
 Volute     To be given by the bidder. 
 Type of Impeller   To be given by the bidder. 
 Pump Speed To be given by the bidder  
  ( Existing Pump speed 742 RPM in both 
Stages) 
  (Technical justification/calculation for 
selected speed shall be provided by the 
bidder with his offer)  
 Provisions of Tapping for flow & pressure measurement in suction & delivery 
side and bearing temperature & vibration (both driving & non driving side) should be 
provided for automation & monitoring through SCADA.    
 
5.30 OPERATING PARAMETERS OF REQUIRED EQUIPMENT  
 
S/L OPERATING PARAMETERS  Stage-Ist  Stage-IInd  
(a) Working period or period of operation Continuous round the year to lift raw water. 
(b) Maximum working head          37.00 M 37.00 M 
(c) Minimum working head  23.00 M 33.00 M 
(d) Maximum NPSH Available 8.24 M 9.42 M 
(e) Minimum NPSH Available 21.54 M 12.22 M 
(f) NPSH Required To be given by the bidder  To be given by the bidder  
 
 
5.40 PERFORMANCE REQUIREMENT  
 The pumps shall be designed and manufactured to satisfy the following 
requirements:- 
(a) The discharge at rated duty point of 37.00 meter head shall be 60 cusec . 
 Requirement of performance characteristics:- 
(b) Discharge Vs. Head curve shall be of rising stable characteristic in whole 
range of operation.  
(c) There shall be no cavitations in whole range of operation of pump. The 
NPSHA shall exceed NPSHR by margin of at least 0.5m.  (d) The efficiency at 37.00 meter head shall not be less than 91% without 
negative tolerances . However, the maximum permissible variation in 
efficiency is (-)5% and it should not be less than 86% in operating range, 
i.e. (+)10% and (-)25% of rated head. Discharge should not be less than 60 
cusec in whole range of operation .  
(e) The pump shall have non-overloading characteristic curve in whole range 
of operation of pump.  
 5.50 The following characteristics curves of the pump shall be submitted by the 
Bidder in readable form:- 
(a) Head v/s Discharge curve  
(b) B.H.P. v/s Discharge curve 
(c) Efficiency v/s Discharge curve  
(d) NPSH (required) v/s Discharge curve   
 
5.60 FOUNDATION   
 The Contractor shall take measurement of existing foundation at site and shall 
ensure the erection of Pumps and Motors on that foundation. The Base Plate 
of Pump and Motor should be common for both. Minor changes can be done 
according to the base plate of the offered Pump set which will lie in the scope 
of the Contractor . 
6.00 MATERIAL OF CONSTRUCTION OF VARIOUS COMPONENTS OF PUMP 
 
The material of construction of the main pump components shall be as mentioned 
below. For rest of the components material of construction shall conform to the 
requirement as per IS:6595 (Part-I)-2002 and IS:5120-1977 or its latest amendments. 
The bidder shall clearly state the composition and related applicable standard of 
material proposed to be used in the manufacture of components. 
 
                     
 
 
 
 
 
 
 
 
 
Test certificate of material of construction/constituents of the main 
pump components shall be provided to third party inspection agency issued 
by NABL accredited lab only  
6.01 SPECIAL CONSTRUCTION FEATURES OF IMPORTANT COMPONENTS 
All the components of pump shall be so designed and manufactured so that 
repair, overhauling and their maintenance is simple apart from optimum life. 
Provisions for data transfer through PLCs etc., for SCADA should be made 
available so that the system when automated may run in Automatic mode. 
Discharge, Head, Suction Pressure, Bearing Temperature (DE & NDE Side), 
etc are the Parameters/Datas which will be required to transmit. 
6.02     CASING  1. Casing Cast Iron FG-260 ( IS:210:1993 ) 
2. Impeller Stainless Steel CA6NM , ASTM-A743, 
3. Shaft Stainless steel AISI-431 
4. Shaft Sleeve Stainless steel AISI-410 (Hardened) 
5. Impeller Wearing  Ring               Stainless Steel CA15NM (hardened), ASTM-A217. 
6. Casing Wearing Ring 2% Ni CI with hardness 210 – 230BHN (The minimum 
difference in hardness of impeller wearing ring and casing 
wearing ring should be 30 BHN). 
7. Pump and Motor 
Coupling Cast steel 
8. Stuffing Box Bush Stainless Steel CA15 with hardness 210-230 BHN. 
9. Nuts & Bolts High Tensile steel Grade 10.8 
10.  Gland Packing Teflon/Asbestos The technical requirement of casing shall be as per IS: 5120-1977. Inside of 
the casing shall be protected by an epoxy glass flake coating  for anti-erosion, 
anti-corrosion and anti-galvanic action to protect the base material of casing 
to facilitate smooth flow. The coating shall be non-toxic, hydrophobic in nature 
and should suit potable water.   
 Firm has to submit Test Certificate issued by any authorized 
National Laboratory that coating shall be non-toxic, hydrophobic in 
nature and suit potable water at the time of Third-Party Inspection & 
time of supply.  
6.03 IMPELLER 
The impeller shall be properly balanced and balance quality grade of impeller 
shall be as per Grade G 6.3 of IS: 11723(Part I):1992. There shall be no 
balancing hole. The shrouded portion of impellers shall be so machined that 
the friction is reduced considerably and in order to achieve better hydraulic 
efficiency, liberally sized wall thickness / vane thickness and double curvature 
vanes shall be preferred apart from it proper location of the leading edges of 
vanes, shall be provided in order to have better life of impeller under adverse 
conditions. 
6.04  WATER PASSAGES 
All the water passages in the casing and the impeller which are inaccessible 
to machining shall be finished to smooth surface as far as possible. 
6.05 STUFFING BOX 
The stuffing box gland shall be split into two halves to facilitate replacement 
of gland packing without removing the driving coupling. 
6.06  LANTERN RING 
In case where a lantern ring is used it shall be sandwiched with the rows of 
packing and shall be easily removable. 
6.07  COUPLING 
Suitable flexible coupling shall be provided with pump to couple it with the 
motor. 
6.08  BEARING 
The bearing may be Ball or Roller or Sleeve type as per design requirement. If 
sleeve bearings are used, they are to be machined for closed running fit. The 
bearing should be designed so as to take up the necessary radial load well as 
the net hydraulic axial thrust and bearing shall be lubricated properly. Where 
there is a possibility of water entering the bearing suitable preventive 
arrangements i.e. water deflectors shall be provided. All the bearing housing 
shall be split into two halves to facilitate easy replacement of bearing.  
6.09 NOISE LEVEL      As per IS-12065 : 1987. 
6.10 VIBRATION LEVEL     As per IS-12075 : 2008. 
6.11 DIRECTION OF ROTATION    As per the site requirement. 
6.12   ACCESSORIES TO BE SUPPLIED WITH PUMP 
Following accessories are to be supplied with pump. 
(a)  Base plate including foundation bolts for pump and motor. 
(b)  Pressure gauge and vacuum gauge for suction and delivery side of pump. 
(c)  Coupling Guards. 
(d)  Suitable Couplings.  
7.00 SPECIAL INSTRUCTIONS 
 
7.10 Bidders are required to furnish following information with their Technical 
offer in Part “B” failing which their offer may be rejected. 
 
 
A. PUMP 
 
  (1.0) Type of Pump 
  (2.0) Model of Pump   (3.0) No. of stages   
(4.0) No. of suction inlet 
(5.0) No. of Volute 
(6.0) Type of Impeller 
(7.0) Suction size in mm dia. 
(8.0) Delivery size in mm dia. 
(9.0) Power at shaft at rated head & discharge. 
(10.0) Speed in revolution per minute. 
(11.0) NPSH required in meters 
(12.0) Discharge & Efficiency at 37.00 meter head   
(13.0) Discharge & Efficiency at (+) 10% and (-) 25% of duty point head. 
(14.0) Drawing showing material of construction of various components of 
pump. 
(15.0) Weight of Pump including base plate & coupling in Kgs. 
(16.0) Sealing Arrangement. 
(17.0) Direction of rotation, when viewing from driving end. 
(18.0)   Noise Level. 
(19.0)   Vibration Level. 
 
Performance Curves:  
(1.0) Head v/s Discharge curve. 
(2.0) B.H.P. v/s Discharge curve. 
(3.0) Efficiency v/s Discharge curve. 
(4.0) NPSH v/s Discharge curve. 
 The above curves should be drawn from shut off to run off condition. 
(5.0) Family curves of the offered model. 
7.20  Following information along-with information mentioned above shall be 
provided by the Contractor after issue of the Acceptance Letter, prior to 
signing of the Contract. 
 
A. PUMP 
  A set of all the performance curves, submitted along with Technical Offer Part 
”B”.                     
(1.0) Head v/s Discharge curve. 
(2.0) B.H.P. v/s Discharge curve. 
(3.0) Efficiency v/s Discharge curve. 
(4.0) NPSH v/s Discharge curve. 
 The above curves should be drawn from shut off to run off condition. 
7.30 Following information/details shall be provided by the Contractor to the 
consignee for his approval, within two weeks after signing of Contract 
and a copy to this Organization. 
 
A. PUMP 
(1.0) General arrangement / lay out drawing of Pump showing important 
dimensions. 
(2.0) Detailed foundation drawing including Block-out / embedment details 
of pump.
"""

response = model.generate_content(NER)
print(response.text)