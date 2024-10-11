$exclude = @("venv", "bot_preco_dolar.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_preco_dolar.zip" -Force