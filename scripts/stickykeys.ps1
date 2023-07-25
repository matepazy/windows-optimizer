$MethodDefinition = @'
[StructLayout(LayoutKind.Sequential)]
public struct STICKYKEYS
{
    public uint cbSize;
    public int dwFlags;
}

[DllImport("user32.dll")]
public static extern int SystemParametersInfo(int uiAction, int uiParam, out STICKYKEYS pvParam, int fWinIni);
'@
$get = 0x003A
$set = 0x003B
$WinApiVariable = Add-Type -MemberDefinition $MethodDefinition -Name 'Win32' -NameSpace '' -PassThru
$startupStickyKeys = New-Object -TypeName 'Win32+STICKYKEYS'
$startupStickyKeys.cbSize = [System.Runtime.InteropServices.Marshal]::SizeOf($startupStickyKeys)
[Win32]::SystemParametersInfo($get, [System.Runtime.InteropServices.Marshal]::SizeOf($startupStickyKeys), [ref]$startupStickyKeys, 0)
Write-Host "Current:"
$startupStickyKeys.dwFlags
Write-host "Set current flag to disabled (506)"
$startupStickyKeys.dwFlags = 506
[Win32]::SystemParametersInfo($set, [System.Runtime.InteropServices.Marshal]::SizeOf($startupStickyKeys), [ref]$startupStickyKeys, 0)