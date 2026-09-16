$ErrorActionPreference = 'Stop'

$docx = (Resolve-Path 'cvs/recommendation_letters/Fatemeh_Torabi_EMBL_EBI_JR3882_Reference_Minimal_Edit.docx').Path
$pdf = Join-Path (Resolve-Path 'cvs/recommendation_letters').Path 'Fatemeh_Torabi_EMBL_EBI_JR3882_Reference_Minimal_Edit_WordExport.pdf'

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.OpenNoRepairDialog($docx, $false, $true, $false, '', '', $true)
    $doc.ExportAsFixedFormat($pdf, 17, $false, 0, 0)
    $doc.Close($false)
    Write-Output $pdf
}
finally {
    $word.Quit()
}
