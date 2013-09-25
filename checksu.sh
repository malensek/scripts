################################################################################
# checksu - function to check if the current user has been su'd to by another
# user.  Returns zero (true) if a su has occurred. 
#
# Example Usage:
# if checksu; then
#     echo "Aha!"
# fi
################################################################################
function checksu() {
    stdin=$(readlink -f /dev/stdin)
    if [[ ! -e "${stdin}" ]]; then # This will fail if non-interactive
        return 1
    else
        [[ $(stat -c '%u' "${stdin}") -ne $(id -u) ]]
    fi
}
