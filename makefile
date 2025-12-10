# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ndahib <ndahib@student.1337.ma>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 17:14:42 by ndahib            #+#    #+#              #
#    Updated: 2025/12/10 18:00:52 by ndahib           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME				:= stokholm

#=== Directories : ============================================================
SRC_DIR				:= src
VENV_DIR			:= .venv
VENV_BIN			:= $(VENV_DIR)/bin

#=== Files : ==================================================================
SRC_FILES			:= ${SRC_DIR}
SRC_MAINE			:= $(SRC_DIR/main.py)
SRC_REQUIREMENTS	:= requirement.txt


#=== Commands : ==============================================================
PYTHON				:=	python
PIP					:= 	pip
RM					:=	rm -rf
PFLAGS				:=	-W default -X dev -b
DESACTIVING_VENV	:= desactivate
#=== Colors 	: =================================================================
DEF					:=	\033[3;39m
GRAY				:=	\033[3;90m
PINK				:=	\033[3;38;5;199m
RED					:=	\033[3;91m
GREEN				:=	\033[3;32m
CYAN				:=	\033[3;96m
PURPLE				:=	\033[3;35m
YELLOW				:=	\033[3;93m
	
#=== Rules :	 ==================================================================
all	: $(VENV_DIR)

$(VENV_DIR):
	@$(PYTHON) -m venv $(VENV_DIR)
	@printf "$(GREEN) [OK] $(YELLOW) Virtual envirenement is created !! $(DEF)\n"

install	:
	@$(VENV_BIN)/$(PIP) install -r $(SRC_REQUIREMENTS)
	@printf "$(GREEN)[OK]$(YELLOW) Dependencies installed!$(DEF)\n"

run	: install
	@if [ ! -f $(VENV_DIR) ]; then\
		printf "(PURPLE) Warning: $(YELLOW) $(VENV_DIR) not found !! $(DEF)\n;"\
	fi
	@if [ ! -f $(NAME) ]; then\
		printf "$(PURPLE) Warning: $(YELLOW) $(NAME) not found !!$(DEF)\n";\
	else\
		make stop > /dev/null;
		if [ -f $(NAME).pid ]; then\
			$(RM) $(NAME).pid;\
		fi;\
		./$(NAME) $(CONFIG_FILE) & printf $$! > $(NAME).pid;\
		printf "$(PURPLE) Notis: $(GREEN) $(NAME) is started!$(DEF) \n";\
	fi

clean:
	@$(DESACTIVING_VENV)

fclean: clean
	@if [ -f $(VENV_DIR) ]; then\
		$(RM) $(VENV_DIR);\
		echo "$(GREEN) [OK]  $(RED) $(NAME) Cleaned!$(DEF)";\
	fi

re:	fclean all

.PHONY: all clean fclean re run stop