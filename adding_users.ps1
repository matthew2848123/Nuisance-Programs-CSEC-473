# Number of users to be created
$numberOfUsers = 50

# Ensure you are running as an administrator
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "You need to run this script as an Administrator!"
    exit
}

# Loop to create local users
for ($i=1; $i -le $numberOfUsers; $i++) {
    $userName = "LocalUser" + $i
    $password = "Password" + $i

    # Create the local user
    $user = New-LocalUser -Name $userName `
                          -Password (ConvertTo-SecureString -String $password -AsPlainText -Force) `
                          -FullName $userName `
                          -Description "Local Admin User with RDP access" `
                          -ErrorAction SilentlyContinue

    # If user creation was successful, grant admin and RDP rights
    if ($user) {
        # Add user to the local 'Administrators' group
        Add-LocalGroupMember -Group "Administrators" -Member $user.Name -ErrorAction SilentlyContinue

        # Add user to the 'Remote Desktop Users' group
        Add-LocalGroupMember -Group "Remote Desktop Users" -Member $user.Name -ErrorAction SilentlyContinue
    } else {
        Write-Warning "Failed to create user $userName."
    }
}

Write-Output "Local users created and added to Administrators and RDP group successfully!"
