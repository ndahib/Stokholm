# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    constants.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ndahib <ndahib@student.1337.ma>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 10:56:00 by ndahib            #+#    #+#              #
#    Updated: 2025/12/13 12:36:07 by ndahib           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

HEADER = "Welcome to Stokholm"
VERSION = "1.0.0"
WANNACRY_EXTENSIONS = """
.der,.pfx,.key,.crt,.csr,.p12,.pem,.odt,.ott,.sxw,.stw,.uot,
.3ds,.max,.3dm,.ods,.ots,.sxc,.stc,.dif,.slk,.wb2,.odp,.otp,
.sxd,.std,.uop,.odg,.otg,.sxm,.mml,.lay,.lay6,.asc,.sqlite3,
.sqlitedb,.sql,.accdb,.mdb,.db,.dbf,.odb,.frm,.myd,.myi,
.ibd,.mdf,.ldf,.sln,.suo,.cs,.c,.cpp,.pas,.h,.asm,.js,
.cmd,.bat,.ps1,.vbs,.vb,.pl,.jsp,.php,.asp,.rb,.java,.jar,
.class,.sh,.mp3,.wav,.swf,.fla,.wmv,.mpg,.vob,.mpeg,.asf,
.avi,.mov,.mp4,.3gp,.mkv,.3g2,.flv,.wma,.mid,.m3u,.m4u,
.djvu,.svg,.ai,.psd,.nef,.tiff,.tif,.cgm,.raw,.gif,.png,
.bmp,.jpg,.jpeg,.vcd,.iso,.backup,.zip,.rar,.7z,.gz,.tgz,
.tar,.bak,.tbk,.bz2,.paq,.arc,.aes,.gpg,.vmx,.vmdk,.vdi,
.sldm,.sldx,.sti,.sxi,.602,.hwp,.snt,.onetoc2,.dwg,.pdf,
.wk1,.wks,.123,.rtf,.csv,.txt,.vsdx,.vsd,.edb,.eml,.msg,
.ost,.pst,.potm,.potx,.ppam,.ppsx,.ppsm,.pp,.ppt,.xlt,
.xl,.xlw,.xlsb,.xlsm,.xlsx,.xls,.dotx,.dotm,.dot,.docm,
.docb,.docx,.doc
"""

EXTENSIONS = {ext.strip().lower() for ext in WANNACRY_EXTENSIONS.split(",") if ext.strip()}

TARGET_DIR = "infection"
EXTENSION = ".ft"
WARNING_FLAG = "warning"
ERROR_FLAG = "error"
SUCCES_FLAG = "succes"

DEF_COLOR   =   "\033[3;39m"
GRAY_COLOR  =	"\033[3;90m"
PINK_COLOR  =	"\033[3;38;5;199m"
RED_COLOR   =	"\033[3;91m"
GREEN_COLOR =	"\033[3;32m"
CYAN_COLOR  =	"\033[3;96m"
PURPLE_COLOR=	"\033[3;35m"
YELLOW_COLOR=	"\033[3;93m"

COLORS = {
    WARNING_FLAG: YELLOW_COLOR,
    ERROR_FLAG: RED_COLOR,
    SUCCES_FLAG: GREEN_COLOR,
}