function Deku {
    param(
        [Parameter(Position=0)]
        [string]$o,
        [Parameter(Position=1)]
        [string]$p
    )
    Start-Process python "<path-to-main.py> $o $p" -NoNewWindow -Wait | Out-Null
}
