import Draft

doc    = App.ActiveDocument
body   = doc.getObject('Body001')
sketch = body.getObject('Sketch002')

vertices = {120: 35,
            126: 34,
            130: 33,
            135: 32,
            142: 31}

for s in (120,126,130,135,142):
    ss = Draft.make_shapestring(String=str(s), FontFile="/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf",
                                Size = 10.,
                                Tracking=0.0)
    ss.AttachmentSupport = [(sketch, (f'Vertex{vertices[s]}',))]
    ss.Justification = u"Middle-Center"
    ss.AttacherEngine = u"Engine Point"
    ss.MapMode = u"Vertex"
    ss.setExpression('Size', u'<<main shape>>.Constraints.thickness / 4.5')
    ss.adjustRelativeLinks(body)
    body.ViewObject.dropObject(ss,None,'',[])
    pocket = body.newObject('PartDesign::Pocket','Pocket')
    pocket.Profile = (ss, ['',])
    pocket.Length = 5
    pocket.UseCustomVector = 0
    pocket.Direction = (0, 0, -1)
    pocket.ReferenceAxis = (ss, ['N_Axis'])
    pocket.AlongSketchNormal = 1
    pocket.Type = 1
    pocket.UpToFace = None
    pocket.Reversed = 1
    pocket.Midplane = 0
    pocket.Offset = 0
