$exclude = @("venv", "bot_kindle.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_kindle.zip" -Force