doc         = App.getDocument('hub_measurement')
body        = doc.Body001
spreadsheet = doc.Spreadsheet

row0 = 3

row = row0
while True:
    try:    config = spreadsheet.get(f'A{row}')
    except: break
    binder = body.newObject('PartDesign::SubShapeBinder',f'Binder_{config}')
    body.removeObject(binder)
    binder.BindCopyOnChange = "Enabled"
    binder.Support          = body
    binder.Configuration    = config
    if (row-row0) & 1:
        m = binder.Placement.Matrix
        m.A11 = m.A22 = -1
        binder.Placement.translate(FreeCAD.Vector(0,100,0))
    binder.Placement.translate(FreeCAD.Vector(100*(row-row0),300,0))
    row += 1
