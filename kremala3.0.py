for o in range(0, 1000, 1):
    word = input('\nΠληκτρολογήστε μια λέξη (χωρίς τόνους)\n')
    word = word.upper()
    word_list = list(word)
    if ' ' in word_list:
        print('\n======================================')
        print('Μη αποδεκτή εισαγωγή.')
        print('Πληκτρολογήστε 1 λέξη.')
        print('======================================\n')
    else:
        wordc = len(word)
        space = ''
        space2 = '_'
        l = 0
        a = 1
        tim = 0
        letlist = list()
        for i in range(1, wordc, 1):
            space += space2
            i += 1
        #########Palaios kwdikas pou den emfanizei tin epanalipsi tou prwtou grammatos efoson yparxei###################
        #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'+word[0]+space.replace('_',' _'))
        #print('\nΗ λέξη που ψάχνετε έχει {} γράμματα.\n'.format(wordc))
        hword = word[0]+space
        hword_list = list(hword)
        i = len(word[0]+space)
        i = i - 2
        p = 6

        temp_list1 = list(word)
        letlist.append(word[0])
        for x in word_list:
            if word[0] in x:
                pos = temp_list1.index(word[0])
                temp_list1.pop(pos)
                temp_list1.insert(pos, " ")
                hword_list.pop(pos)
                hword_list.insert(pos, word[0])
                stra = ""
                for elee in hword_list:
                    stra += elee
                stra = stra.replace('_',' _')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                print(' _______')
                print('|    |')
                print('|')
                print('|')
                print('|')
                print('|')
                print('========')
                print('\n======================================\n')
                print(stra)
                print('\nΗ λέξη που ψάχνετε έχει {} γράμματα.\n'.format(wordc))

        while '_' in hword_list and l <6:
            letter = input('Παρακαλώ πληκτρολογήστε το επόμενο γράμμα:')
            letter = letter.upper()
            letterc = len(letter)
            if letterc > 1 or letterc == 0 or letter == ' ':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                print('\n======================================')
                print('Μη αποδεκτή εισαγωγή.')
                print('Πληκτρολογήστε 1 γράμμα.')
                print('======================================\n')
                if p == 6:
                    print(' _______')
                    print('|    |')
                    print('|')
                    print('|')
                    print('|')
                    print('|')
                    print('========')
                elif p == 5:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|')
                    print('|')
                    print('|')
                    print('========')
                elif p == 4:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|    |')
                    print('|')
                    print('|')
                    print('========')
                elif p == 3:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|   /|')
                    print('|')
                    print('|')
                    print('========')
                elif p == 2:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|   /|\ ')
                    print('|')
                    print('|')
                    print('========')
                elif p == 1:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|   /|\ ')
                    print('|   / ')
                    print('|')
                    print('========')
                elif p == 0:
                    print(' _______')
                    print('|    |')
                    print('|    O')
                    print('|   /|\ ')
                    print('|   / \ ')
                    print('|')
                    print('========')
                print('\n======================================\n')
                letter = letter.upper()
                str1 = ""
                for ele in hword_list:
                    str1 += ele
                str1 = str1.replace('_','_ ')
                print(str1+'\n')
            else:
                if letter in letlist:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                    print('\n======================================')
                    print('Έχετε εισάγει ξανά αυτό το γράμμα.')
                    print('======================================\n')
                    if p == 6:
                        print(' _______')
                        print('|    |')
                        print('|')
                        print('|')
                        print('|')
                        print('|')
                        print('========')
                    elif p == 5:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|')
                        print('|')
                        print('|')
                        print('========')
                    elif p == 4:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|    |')
                        print('|')
                        print('|')
                        print('========')
                    elif p == 3:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|   /|')
                        print('|')
                        print('|')
                        print('========')
                    elif p == 2:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|   /|\ ')
                        print('|')
                        print('|')
                        print('========')
                    elif p == 1:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|   /|\ ')
                        print('|   / ')
                        print('|')
                        print('========')
                    elif p == 0:
                        print(' _______')
                        print('|    |')
                        print('|    O')
                        print('|   /|\ ')
                        print('|   / \ ')
                        print('|')
                        print('========')
                    print('\n======================================\n')                    
                    str1 = ""
                    for ele in hword_list:
                        str1 += ele
                    str1 = str1.replace('_','_ ')
                    print(str1+'\n')
                    str2 = ''
                    for ala in letlist:
                        str2 += ala+', '
                    print('Ιστορικό προσπαθειών:\n'+str2)
                else:
                    temp_list = list(word)
                    tim = 0
                    letlist.append(letter)
                    for x in word_list:
                        if letter in x:
                            pos = temp_list.index(letter)
                            tim = word_list.count(letter)
                            temp_list.pop(pos)
                            temp_list.insert(pos, " ")
                            hword_list.pop(pos)
                            hword_list.insert(pos, letter)
                    if tim > 1:
                        if '_' in hword_list:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if p == 6:
                                print(' _______')
                                print('|    |')
                                print('|')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 5:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 4:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|    |')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 3:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 2:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 1:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / ')
                                print('|')
                                print('========')
                            elif p == 0:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / \ ')
                                print('|')
                                print('========')
                            print('\n======================================\n')
                            print('Σωστά! Το γράμμα {}, υπάρχει {} φορές!\n'.format(letter, tim))
                            str1 = ""
                            for ele in hword_list:
                                str1 += ele
                            str1 = str1.replace('_','_ ')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        else:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if p == 6:
                                print(' _______')
                                print('|    |')
                                print('|')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 5:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 4:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|    |')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 3:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 2:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 1:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / ')
                                print('|')
                                print('========')
                            elif p == 0:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / \ ')
                                print('|')
                                print('========')
                            print('\n======================================\n')
                            str1 = ''
                            for ele in hword_list:
                                str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            print('Συγχαρητήρια! Κερδίσατε!')
                    elif tim == 1:
                        if '_' in hword_list:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if p == 6:
                                print(' _______')
                                print('|    |')
                                print('|')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 5:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 4:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|    |')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 3:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 2:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 1:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / ')
                                print('|')
                                print('========')
                            elif p == 0:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / \ ')
                                print('|')
                                print('========')
                            print('\n========================================\n')
                            print('Σωστά! Το γράμμα {}, υπάρχει {} φορά!\n'.format(letter, tim))
                            str1 = ""
                            for ele in hword_list:
                                str1 += ele
                            str1 = str1.replace('_','_ ')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        else:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if p == 6:
                                print(' _______')
                                print('|    |')
                                print('|')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 5:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 4:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|    |')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 3:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 2:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|')
                                print('|')
                                print('========')
                            elif p == 1:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / ')
                                print('|')
                                print('========')
                            elif p == 0:
                                print(' _______')
                                print('|    |')
                                print('|    O')
                                print('|   /|\ ')
                                print('|   / \ ')
                                print('|')
                                print('========')
                            print('\n======================================\n')
                            str1 = ''
                            for ele in hword_list:
                                str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            print('Συγχαρητήρια! Κερδίσατε!\n')
                    elif tim == 0:
                        l += 1
                        p = 6-l
                        if p == 5:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|')
                            print('|')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λάθος, το γράμμα {} δεν υπάρχει. \nΈχετε ακόμα '.format(letter)+str(p)+' προσπάθειες, προσπαθήστε ξανά!\n')
                            str1 = ''
                            for ele in hword_list:
                              str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        elif p == 4:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|    |')
                            print('|')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λάθος, το γράμμα {} δεν υπάρχει. \nΈχετε ακόμα '.format(letter)+str(p)+' προσπάθειες, προσπαθήστε ξανά!\n')
                            str1 = ''
                            for ele in hword_list:
                              str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        elif p == 3:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|   /|')
                            print('|')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λάθος, το γράμμα {} δεν υπάρχει. \nΈχετε ακόμα '.format(letter)+str(p)+' προσπάθειες, προσπαθήστε ξανά!\n')
                            str1 = ''
                            for ele in hword_list:
                              str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        elif p == 2:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|   /|\ ')
                            print('|')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λάθος, το γράμμα {} δεν υπάρχει. \nΈχετε ακόμα '.format(letter)+str(p)+' προσπάθειες, προσπαθήστε ξανά!\n')
                            str1 = ''
                            for ele in hword_list:
                              str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        elif p == 1:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|   /|\ ')
                            print('|   / ')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λάθος, το γράμμα {} δεν υπάρχει. \nΈχετε ακόμα '.format(letter)+str(p)+' προσπάθειες, προσπαθήστε ξανά!\n')
                            str1 = ''
                            for ele in hword_list:
                              str1 += ele
                            str1 = str1.replace('_',' _')
                            print(str1+'\n')
                            str2 = ''
                            for ala in letlist:
                                str2 += ala+', '
                            print('Ιστορικό προσπαθειών:\n'+str2)
                        elif p <= 0:
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            print(' _______')
                            print('|    |')
                            print('|    O')
                            print('|   /|\ ')
                            print('|   / \ ')
                            print('|')
                            print('========')
                            print('\n======================================\n')
                            print('Λυπάμαι, χάσατε.\n')
                            print('Η λέξη ήταν '+word+'!')
        print('Τέλος παιχνιδιού\n')
        print('======================================')
        print('======================================\n\n\n\n')
