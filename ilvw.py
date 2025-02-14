import os
import random

DICTIONARY_DIR = "word"
WRONG_WORD = os.path.join(DICTIONARY_DIR, "错词本.txt")

def init_env():
    if not os.path.exists(DICTIONARY_DIR):
        os.makedirs(DICTIONARY_DIR)
    if not os.path.exists(WRONG_WORD):
        open(WRONG_WORD, 'a').close()

def get_dictionarys():
    dictionarys = []
    for f in os.listdir(DICTIONARY_DIR):
        if f.endswith(".txt") and f != "错词本.txt":
            with open(os.path.join(DICTIONARY_DIR, f), 'r', encoding='utf-8') as file:
                count = len([line for line in file if line.strip()])
            dictionarys.append((f, count))
    return sorted(dictionarys, key=lambda x: x[0])

def show_dictionarys(dictionarys):
    print("\n可用单词本：")
    for i, (name, count) in enumerate(dictionarys, 1):
        print(f"{i}. {name[:-4]}（{count}个单词）")

def add_words():
    dictionarys = get_dictionarys()
    show_dictionarys(dictionarys)
    
    choice = input("\n请选择单词本序号（N新建）：")
    if choice.upper() == 'N':
        name = input("请输入新单词本名称：") + ".txt"
        filepath = os.path.join(DICTIONARY_DIR, name)
        open(filepath, 'a').close()
    else:
        filepath = os.path.join(DICTIONARY_DIR, dictionarys[int(choice)-1][0])
    
    while True:
        en = input("\n输入外文（Q退出）：").strip()
        if en.upper() == 'Q': break
        cn = input("输入中文：").strip()
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"{en}:{cn}\n")
    print("录入完成！")

def view_dictionarys():
    dictionarys = get_dictionarys()
    show_dictionarys(dictionarys)
    
    choice = input("\n请选择要查看的单词本序号：")
    filepath = os.path.join(DICTIONARY_DIR, dictionarys[int(choice)-1][0])
    with open(filepath, 'r', encoding='utf-8') as f:
        print(f"\n【{dictionarys[int(choice)-1][0][:-4]}】单词表：")
        for line in f:
            en, cn = line.strip().split(':')
            print(f"{en} -> {cn}")

def practice():
    dictionarys = get_dictionarys()
    show_dictionarys(dictionarys)
    
    choice = input("\n请选择单词本（序号/A-所有/W-错题）：").upper()
    if choice == 'A':
        words = []
        for book in dictionarys:
            with open(os.path.join(DICTIONARY_DIR, book[0]), 'r', encoding='utf-8') as f:
                words.extend([line.strip() for line in f])
    elif choice == 'W':
        with open(WRONG_WORD, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f]
    else:
        with open(os.path.join(DICTIONARY_DIR, dictionarys[int(choice)-1][0]), 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f]
    
    try:
        num = int(input("要背多少个单词？"))
        random.shuffle(words)
        correct = 0
        for item in random.sample(words, min(num, len(words))):
            en, cn = item.split(':')
            answer = input(f"\n中文：{cn}\n请输入外文：").strip()
            if answer != en:
                print(f"错误！正确答案：{en}")
                with open(WRONG_WORD, 'a', encoding='utf-8') as f:
                    f.write(f"{en}:{cn}\n")
            else:
                print("正确！")
                correct += 1
        print(f"\n测试完成，正确率：{correct}/{min(num, len(words))} ({correct/min(num, len(words))*100:.1f}%)")
    except ValueError:
        print("输入无效！")

def view_wrongwords():
    with open(WRONG_WORD, 'r', encoding='utf-8') as f:
        count = len([line for line in f if line.strip()])
        print("\n【错词本】 "+ str(count) +" 个错误单词")
    with open(WRONG_WORD, 'r', encoding='utf-8') as f:
        for line in f:
            en, cn = line.strip().split(':')
            print(f"{en} --> {cn}")

def main():
    init_env()
    while True:
        print("\n" + "="*30)
        print("1 录入新单词\n2 查看单词本\n3 背单词\n4 查看错词本\n5 退出")
        choice = input("请选择操作：")
        
        if choice == '1':
            add_words()
        elif choice == '2':
            view_dictionarys()
        elif choice == '3':
            practice()
        elif choice == '4':
            view_wrongwords()
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效输入！")

if __name__ == "__main__":
    main()
