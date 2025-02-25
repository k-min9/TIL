# 내가 만든 스토리지 이름으로 training image의 info가 담긴 json의 정보를 바꾸라는 powershell
$storageAcct = 'customclassifycnskm994'
(Get-Content training-images/training_labels.json) -replace '<storageAccount>', $storageAcct | Out-File training-images/training_labels.json