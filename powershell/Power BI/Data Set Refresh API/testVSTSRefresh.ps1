# Testing refresh API following steps from manageRefresh.ps1

# dataset url: https://app.powerbi.com/groups/c061e059-ef03-470a-828d-5c5e5a097008/datasets/d7af7c72-9ad3-4e81-b333-b88e0e630cfd
# groupID=c061e059-ef03-470a-828d-5c5e5a097008
# datasetID=d7af7c72-9ad3-4e81-b333-b88e0e630cfd

$groupID = "c061e059-ef03-470a-828d-5c5e5a097008"
$datasetID = "d7af7c72-9ad3-4e81-b333-b88e0e630cfd"

# Registered app at: https://dev.powerbi.com/apps

$clientID = "5fe5593b-c717-439c-9402-8dffaec176dd"

function GetAuthToken
{
       $adal = "${env:ProgramFiles(x86)}\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\Services\Microsoft.IdentityModel.Clients.ActiveDirectory.dll"
 
       $adalforms = "${env:ProgramFiles(x86)}\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\Services\Microsoft.IdentityModel.Clients.ActiveDirectory.WindowsForms.dll"
 
       [System.Reflection.Assembly]::LoadFrom($adal) | Out-Null
 
       [System.Reflection.Assembly]::LoadFrom($adalforms) | Out-Null
 
       $redirectUri = "urn:ietf:wg:oauth:2.0:oob"
 
       $resourceAppIdURI = "https://analysis.windows.net/powerbi/api"
 
       $authority = "https://login.microsoftonline.com/common/oauth2/authorize";
 
       $authContext = New-Object "Microsoft.IdentityModel.Clients.ActiveDirectory.AuthenticationContext" -ArgumentList $authority
 
       $authResult = $authContext.AcquireToken($resourceAppIdURI, $clientId, $redirectUri, "Auto")
 
       return $authResult
}

# Get the auth token from AAD
$token = getAuthToken

# Building Rest API header with auth token
$authHeader = @{
    'Content-Type'='application/json'
    'Authorization'=$token.CreateAuthorizationHeader()
}

# properly format groups path
$groupsPath = ""
if ($groupID -eq "me") {
    $groupsPath = "myorg"
} else {
    $groupsPath = "myorg/groups/$groupID"
}

# Refresh the dataset
$uri = "https://api.powerbi.com/v1.0/$groupsPath/datasets/$datasetID/refreshes"
Invoke-RestMethod -Uri $uri –Headers $authHeader –Method POST –Verbose

# Check the refresh history
$uri = "https://api.powerbi.com/v1.0/$groupsPath/datasets/$datasetID/refreshes"
Invoke-RestMethod -Uri $uri –Headers $authHeader –Method GET –Verbose
