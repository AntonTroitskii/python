import re


# list anatomy for adult protocols
ANATOMY_LIST = ['ADULT HEAD', 'ADULT ORBIT', 'ADULT CSPINE', 'ADULT SHOULDER', 'ADULT CHEST',
                'ADULT ABDOMEN', 'ADULT LUMBAR', 'ADULT PELVIS', 'ADULT LOWER EXTREMITY', 'ADULT MISCELLANEOUS']

ANATOMY_PATTERN_LIST = list(
    map(lambda x: x + r'\s\d{1,2}\.\d{1,2}.+', ANATOMY_LIST))

#regex pattern for all adult anatomies
ANATOMY_PATTERN = '|'.join(ANATOMY_PATTERN_LIST)




# ADULT HEAD 1.1 Head (adult) 1.25
# ADULT HEAD 1.2 Head Contrast (adult) 1.25 N+C
# ADULT HEAD 1.4 Head SRS (adult) 0.625
# ADULT HEAD 1.5 Head SRS Contrast (adult) 0.625 N+C
# ADULT HEAD 1.19 Routine Head Axial 2.5/5mm n+c
# ADULT HEAD 1.20 Helical Head Auto 5mm n+c
# ADULT HEAD 1.21 Circle of Willis n+c
# ADULT HEAD 1.23 BCA n(head)+c
# ADULT HEAD 1.24 Physicist Head (adult) 1.25 MAR
# ADULT HEAD 1.25 Physicist Head_SRS (adult) 0.625
# ADULT HEAD 1.27 Head SRS 0.625 120kV axial 0.625
# ADULT HEAD 1.28 Head SRS 0.625 120kV axial 0.625 contrast n+c
# ADULT ORBIT 2.16 Sinus Supine  Helical
# ADULT ORBIT 2.17 Helical IAC 0.625mm R2R3
# ADULT ORBIT 2.22 HeadNeck (adult) 1.25 GE SEMEN
# ADULT ORBIT 2.23 HeadNeck_SRS (adult) 0.625 GE SEMEN
# ADULT ORBIT 2.24 HeadNeck_Contrast(adult) 1.25 n+c(a+v) GE SEMEN
# ADULT ORBIT 2.25 HeadNeck_SRS_Contrast(adult) 0.625 n+c(a+v) GE SEMEN
# ADULT ORBIT 2.27 HeadNeck (adult) 1.25 GE SEMEN
# ADULT ORBIT 2.28 HeadNeck (adult) 1.25 GE SEMEN
# ADULT ORBIT 2.29 HeadNeck_Contrast(adult) 1.25 n+c(a+v) GE SEMEN
# ADULT ORBIT 2.30 HeadNeck_SRS_Contrast(adult) 0.625 n+c(a+v) GE SEMEN
# ADULT CSPINE 3.1 HeadNeck (adult) 1.25
# ADULT CSPINE 3.2 HeadNeck Contrast (adult) 1.25 N+C(A+V)
# ADULT CSPINE 3.4 HeadNeck SRS (adult) 0.625
# ADULT CSPINE 3.5 HeadNeck SRS Contrast (adult) 0.625 N+C(A+V)
# ADULT CSPINE 3.16 Soft Tissue Neck n+c(a+d)+d
# ADULT CSPINE 3.27 Head_Neck (adult) 1.25 MAR GE SEMEN
# ADULT CSPINE 3.28 Head_Neck_SRS (adult) 0.625 MAR GE SEMEN
# ADULT CSPINE 3.29 Head_Neck_Contrast (adult)1.25 n+c(a+v) MAR GE SEMEN
# ADULT CSPINE 3.30 Head_Neck_Contrast_SRS (adult) 0.625 n+c(a+v) MAR GE SEMEN
# ADULT SHOULDER 4.13 Breast (adult) 1.25 GE SEMEN
# ADULT SHOULDER 4.14 Breast_DIBH (adult) N+DIBH GE SEMEN
# ADULT SHOULDER 4.15 Breast_DIBH_4DCT (adult) GE SEMEN
# ADULT SHOULDER 4.16 Shoulder
# ADULT SHOULDER 4.28 Breast (adult) 1.25 GE SEMEN
# ADULT SHOULDER 4.29 Breast_DIBH (adult) N+DIBH GE SEMEN
# ADULT SHOULDER 4.30 Breast_DIBH_4DCT (adult) GE SEMEN
# ADULT SHOULDER 4.17 Ulnar R2R3
# ADULT CHEST 5.1 Breast (adult) 1.25mm
# ADULT CHEST 5.2 Breast_DIBH (adult) N+DBIH 1.25mm
# ADULT CHEST 5.3 Breast_DIBH_4DCT (adult) 1.25 ?
# ADULT CHEST 5.5 Thorax (adult) 1.25mm
# ADULT CHEST 5.6 Thorax_4D (adult) N+4D 1.25mm
# ADULT CHEST 5.7 Thorax_Contrast (adult) N(Free)+N(DIBH)+C(A+V) 1.25mm
# ADULT CHEST 5.8 Thorax_Contrast (adult) N(Free)+N(DIBH)+C(A+V)+4D 1.25mm
# ADULT CHEST 5.10 Thorax_SRS (adult) 0.625mm
# ADULT CHEST 5.12 Thorax (adult) 1.25mm Slow Helical+Axial
# ADULT CHEST 5.13 Thorax (adult) 1.25mm Slow Helical+Axial+C(A+V)
# ADULT CHEST 5.16 Routine Chest n+c(a+v)
# ADULT CHEST 5.22 Breast (adult) 1.25 GE SEMEN
# ADULT CHEST 5.23 Breast_DIBH (adult) N+DBIH GE SEMEN
# ADULT CHEST 5.24 Breast_DIBH_4DCT (adult) GE SEMEN
# ADULT CHEST 5.25 Thorax (adult) GE SEMEN
# ADULT CHEST 5.26 Thorax_4D (adult) N+4D GE SEMEN
# ADULT CHEST 5.27 Thorax_Contrast (adult) N(Free)+n(DIDH)+C(A+V) GE SEMEN
# ADULT CHEST 5.28 Thorax_Contrast_4D (adult) N(Free)+n(DIBH)+C(A+V)+4D GE SEME
# ADULT CHEST 5.29 Thorax_SRS (adult) 0.625 GE SEMEN
# ADULT CHEST 5.31 Breast (adult) Klarity Phantom 1.25mm
# ADULT CHEST 5.33 Breast (adult) 1.25mm
# ADULT CHEST 5.34 Breast_DIBH (adult) N+DBIH 1.25mm (PREVIOUS)
# ADULT CHEST 5.30 Thorax_SRS_Contrast (adult) 0.625 n+c(a+v) GE SEMEN
# ADULT ABDOMEN 6.1 Abdomen (adult) 1.25mm
# ADULT ABDOMEN 6.2 Abdomen Contrast (adult) 1.25mm N(Free)+N(DIBH)+C(A+V+D)
# ADULT ABDOMEN 6.3 Abdomen Contrast 4D (adult) 1.25mm N(F)+N(DIBH)+c(A+V+D)
# ADULT ABDOMEN 6.4 Abdomen Contrast Diagnostic 1.25mm (adult) N+C(A+V+D)
# ADULT ABDOMEN 6.5 Abdomen Extretory (adult) 1.25mm
# ADULT ABDOMEN 6.7 Abdomen SRS (adult) 0.625mm
# ADULT ABDOMEN 6.8 Abdomen SRS Contrast (adult) 0.625mm N(F)+N(DIBH)+C(A+V)
# ADULT ABDOMEN 6.10 Abdomen (adult) 1.25mm MAR
# ADULT ABDOMEN 6.16 Dual phase n+c(a+v)+d
# ADULT ABDOMEN 6.18 Chest Abdomen n+c(a+v)+d
# ADULT ABDOMEN 6.20 Abdomen_Contrast 1.25 (adult) n(Free)+n(DIBH)+c(a+v+d) TEST
# ADULT ABDOMEN 6.24 Abdomen (adult) 1.25 mar GE SEMEN
# ADULT ABDOMEN 6.25 Abdomen (adult) 1.25 GE SEMEN
# ADULT ABDOMEN 6.26 Abdomen_Contrast 1.25 (adult) n(Free)+n(DIBH)+c(a+v+d) GE SE
# ADULT ABDOMEN 6.27 Abdomen_Contrast 4D (adult) GE SEMEN
# ADULT ABDOMEN 6.28 Abdomen_Contrast Diagnostic 1.25 (adult) n+c(a+v+d) GE SEMEN
# ADULT ABDOMEN 6.29 Abdomen_SRS (adult) 0.625_GE SEMEN
# ADULT ABDOMEN 6.30 Abdomen_SRS_Contrast (adult) 0.625 GE SEMEN
# ADULT LUMBAR 7.17 L-Spine Survey >100kg
# ADULT LUMBAR 7.18 L-Spine Survey &lt;100kg
# ADULT LUMBAR 7.19 L-Spine Survey 2.5mm MAR
# ADULT LUMBAR 7.30 Abdomen (adult) 1.25 mar GE SEMEN
# ADULT LUMBAR 7.16 L-Spine 
# ADULT PELVIS 8.1 Pelvis (Adult) 1.25mm
# ADULT PELVIS 8.2 Pelvis Contrast (Adult) 1.25mm
# ADULT PELVIS 8.3 Pelvis Extretory (Adult) 1.25mm
# ADULT PELVIS 8.4 Pelvis Catheter (Adult) 1.25mm
# ADULT PELVIS 8.6 Pelvis SRS(Adult) 0.625mm
# ADULT PELVIS 8.7 Pelvis SRS Contrast(Adult) 0.625mm
# ADULT PELVIS 8.8 Pelvis SRS Extretory (Adult) 0.625mm
# ADULT PELVIS 8.9 Pelvis SRS Catheter (Adult) 0.625mm
# ADULT PELVIS 8.15 Pelvis_SRS(Adult)0.625 2021-10-29
# ADULT PELVIS 8.16 TEST Pelvis_Contrast 1.25 (Adult) n+c(a+v)
# ADULT PELVIS 8.22 Pelvis (Adult) 1.25 GE SEMEN
# ADULT PELVIS 8.23 Pelvis_Contrast 1.25 (Adult) n+c(a+v) GE SEMEN
# ADULT PELVIS 8.24 Pelvis_SRS(Adult)0.625 GE SEMEN
# ADULT PELVIS 8.25 Pelvis_SRS_Contrast(Adult) 0.625 n+c(a+v) GE SEMEN
# ADULT PELVIS 8.27 Pelvis (Adult) MAR GE SEMEN
# ADULT PELVIS 8.28 Pelvis_Contrast (Adult) MAR GE SEMEN
# ADULT PELVIS 8.29 Pelvis_SRS(Adult) MAR GE SEMEN
# ADULT PELVIS 8.30 Pelvis_SRS_Contrast(Adult)MAR
# ADULT LOWER EXTREMITY 9.1 Leg (Adult) MAR 1.25mm 
# ADULT LOWER EXTREMITY 9.2 Leg Contrast 1.25 (Adult) N+C(A+V)
# ADULT LOWER EXTREMITY 9.16 Hip Joint 0.625mm  MAR
# ADULT LOWER EXTREMITY 9.19 Leg (Adult) 1.25 GE SEMEN
# ADULT LOWER EXTREMITY 9.20 Leg_Contrast 1.25 (Adult) n+c(a+v) GE SEMEN
# ADULT LOWER EXTREMITY 9.22 Leg (Adult) MAR GE SEMEN
# ADULT LOWER EXTREMITY 9.23 Leg_Contrast (Adult) MAR GE SEMEN
# ADULT LOWER EXTREMITY 9.17 Ankle 1.25 mm 
# ADULT MISCELLANEOUS 10.1 QA_phantom
# ADULT MISCELLANEOUS 10.2 Head_calc_ax
# ADULT MISCELLANEOUS 10.3 Head_calc_helical
# ADULT MISCELLANEOUS 10.5 TEST Lap QA
# ADULT MISCELLANEOUS 10.17 AT_Patient_Position_Accuracy
# ADULT MISCELLANEOUS 10.18 AT_Preview_Image_Accuracy_Test
# ADULT MISCELLANEOUS 10.19 AT_Tomographic_Section_Thickness
# ADULT MISCELLANEOUS 10.20 AT_Head_Noise_Mean_CT_Number_and_Uniformity
# ADULT MISCELLANEOUS 10.21 AT_Spatial_Resolution
# ADULT MISCELLANEOUS 10.22 AT_Low_Contrast_Resolution
# ADULT MISCELLANEOUS 10.23 AT_Dose_Positioning Head
# ADULT MISCELLANEOUS 10.24 AT_Dose_Positioning Body
# ADULT MISCELLANEOUS 10.25 AT_Dose_Head 16CTDI N=10
# ADULT MISCELLANEOUS 10.26 AT_Dose_Large_Head 16CTDI N=10
# ADULT MISCELLANEOUS 10.27 AT_Dose_Small 32CTDI N=10
# ADULT MISCELLANEOUS 10.28 AT_Dose_Large 32CTDI N=10
# ADULT MISCELLANEOUS 10.29 AT_Dose_Air 
