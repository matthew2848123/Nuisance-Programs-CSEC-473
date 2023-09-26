#Matthew Repecki
# Cyber Defense Techniques, Fall 2023
# Team Bravo
# Array of languages to loop through
$languages = @(
    'de-DE',    # German (Germany)
    'pt-BR',    # Portuguese (Brazil)
    'nl-NL',    # Dutch (Netherlands)
    'sv-SE',    # Swedish (Sweden)
    'ru-RU',    # Russian (Russia)
    'zh-CN',    # Chinese (Simplified, China)
    'ja-JP',    # Japanese (Japan)
    'ko-KR',    # Korean (Korea)
    'ar-SA',    # Arabic (Saudi Arabia)
    'hi-IN',    # Hindi (India)
    'pl-PL'     # Polish (Poland)
)

# Loop through each language, set the language, and wait for 180 seconds
foreach ($lang in $languages) {
    Write-Host "Setting language to: $lang"
    Set-WinUILanguageOverride -Language $lang
    Set-WinUserLanguageList $lang -Force
    Set-WinSystemLocale $lang
    Start-Sleep -Seconds 20
}
