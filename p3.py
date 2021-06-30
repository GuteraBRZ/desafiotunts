from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from math import ceil

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)

client = gspread.authorize(creds)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1vvMtqLQlXoLJVVeOTNgpZuUC4Vg7WQl_ArasiPlB8GQ'

service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API

#M1
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C4:F4').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G4'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M2
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C5:F5').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G5'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M3
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C6:F6').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G6'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M4
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C7:F7').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G7'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M5
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C8:F8').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G8'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M6
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C9:F9').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G9'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M7
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C10:F10').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G10'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M8
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C11:F11').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G11'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M9
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C12:F12').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G12'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M10
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C13:F13').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G13'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M11
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C14:F14').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G14'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M12
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C15:F15').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G15'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M13
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C16:F16').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G16'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M14
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C17:F17').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G17'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M15
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C18:F18').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G18'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M16
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C19:F19').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G19'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M17
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C20:F20').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G20'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M18
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C21:F21').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G21'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M19
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C22:F22').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G22'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M20
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C23:F23').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G23'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M21
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C24:F24').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G24'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M22
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C25:F25').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G25'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M23
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C26:F26').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G26'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()

#M24
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='engenharia_de_software!C27:F27').execute()
value = result.get('values')
value = ''.join(str(elem) for elem in value)
value=value.replace('[','')
value=value.replace(']','')
f = int(value[1:3])
p1 = int(value[7:9])
p2 = int(value[13:15])
p3 = int(value[19:21])

rf=f/60
m=(p1+p2+p3)/3
naf=100-m
naf=ceil(naf)
rpf=[['Reprovado por Falta',0]]
exf=[['Exame Final',naf]]
apr=[['Aprovado',0]]
rpn=[['Reprovado por Nota',0]]
rgout='engenharia_de_software!G27'
if(rf > 0.25):
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpf}).execute()
elif(m>=70):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":apr}).execute()
elif(50>m):
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":rpn}).execute()
else:
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rgout, valueInputOption='USER_ENTERED',body={"values":exf}).execute()
