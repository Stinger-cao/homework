#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ܽ���
���ڣ�2020/4/1
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        player=int(0)
    elif name=="ʷ����":
        player=int(1)
    elif name=="��":
	    player=int(2)
    elif name=="����":
	    player=int(3)
    elif name=="����":
        player=int(4)
    else:
	    player=int(5)
    return player

   


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    if  number ==0: #��ת��Ϊʯͷ����������ʷ����
	    computer=str("ʯͷ")
    elif number ==  1:
        computer=str("ʷ����")
    elif number == 2 :
        computer=str("��")
    elif number == 3:
	    computer=str("����" )
    else :	 
	    computer=str("����")
    return computer


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice= name_to_number(choice_name)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    import random
    comp_number=int(random.randint(0,4)) # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    computer_choice_name= number_to_name(comp_number) # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("�������ѡ��Ϊ��", computer_choice_name)# ����Ļ����ʾ�����ѡ����������
    if ((player_choice == 4 and comp_number == 2)or (player_choice == 2 and comp_number == 0) # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
	or (player_choice == 0 and comp_number == 4)or(player_choice == 0 and comp_number == 3)
	or(player_choice == 3 and comp_number == 1)or (player_choice == 1 and comp_number == 4)
	or (player_choice == 1 and comp_number == 0)or (player_choice == 3 and comp_number == 2)
	or (player_choice == 2 and comp_number == 1)or (player_choice == 4 and comp_number == 3)):
        return("��Ӯ�ˣ�")
    elif player_choice == comp_number:
	    return("ƽ���ˣ�") # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    elif player_choice ==5:
        return("Error: No Correct Name")
    else:
        return("����Ӯ�ˣ�")
    
print("��ӭʹ��RPSLS��Ϸ")
print("----------------") # ���"-------- "���зָ�
print("����������ѡ��:") # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
choice_name=input()
print("����ѡ��Ϊ",choice_name)
print(rpsls(choice_name))

