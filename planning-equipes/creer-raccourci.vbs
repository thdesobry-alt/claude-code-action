' Cree le raccourci "PLANNING" sur le Bureau, avec l'icone du planning.
' A placer dans le meme dossier que index.html et icone-planning.ico, puis double-cliquer.
Option Explicit
Dim fso, sh, dossier, cible, ico, local, raccourci, lnk
Set fso = CreateObject("Scripting.FileSystemObject")
Set sh = CreateObject("WScript.Shell")
dossier = fso.GetParentFolderName(WScript.ScriptFullName)
cible = fso.BuildPath(dossier, "index.html")
ico = fso.BuildPath(dossier, "icone-planning.ico")
If Not fso.FileExists(cible) Or Not fso.FileExists(ico) Then
  MsgBox "index.html ou icone-planning.ico est introuvable dans : " & dossier, 48, "Planning des equipes"
  WScript.Quit 1
End If
' Copie locale de l'icone : Windows affiche mal une icone situee sur un lecteur reseau ou OneDrive.
local = sh.ExpandEnvironmentStrings("%LOCALAPPDATA%") & "\PlanningEquipes"
If Not fso.FolderExists(local) Then fso.CreateFolder local
fso.CopyFile ico, local & "\icone-planning.ico", True
raccourci = sh.SpecialFolders("Desktop") & "\PLANNING.lnk"
Set lnk = sh.CreateShortcut(raccourci)
lnk.TargetPath = cible
lnk.WorkingDirectory = dossier
lnk.IconLocation = local & "\icone-planning.ico,0"
lnk.Description = "Planning des equipes"
lnk.Save
MsgBox "Raccourci PLANNING cree sur le Bureau.", 64, "Planning des equipes"
