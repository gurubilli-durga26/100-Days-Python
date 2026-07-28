#ATM machine
ICIC_Durga={'name':'Durga',
            'ADR':'23456789',
            'PAN':'QWE234RTY',
            'ATM PIN':'3456',
            'BALANCE':6500,
            'Transaction':[]}
remain_A=3
while remain_A>0:
    pin=input('enter your 4 digit pin:')
    if len(pin)==4:
        if pin in ICIC_Durga['ATM PIN']:
            option=int(input('Enter \n1.Withdraw \n2.Deposit \n3.Balance \n4.Exit:'))
            if option==1:
                withdraw_m=int(input('Enter amount you want to withdraw:'))
                if withdraw_m<=ICIC_Durga['BALANCE'] and withdraw_m%100==0:
                    ICIC_Durga['BALANCE']-=withdraw_m
                    ICIC_Durga['Transaction'].append(f'withdraw:-{withdraw_m}')
                    print(f'you have withdraw {withdraw_m} and the total balance {ICIC_Durga['BALANCE']}')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
                else:
                    print('can not provide change or no balance')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
            elif option==2:
                deposit_m=int(input('Enter the money you want to deposit:'))
                if deposit_m%100==0:
                    ICIC_Durga['BALANCE']+=deposit_m
                    ICIC_Durga['Transaction'].append(f'deposit:+{deposit_m}')
                    print(f'you have deposited {deposit_m} and the total balance{ICIC_Durga['BALANCE']}')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
                        user=int(input('Enter \n1.Home page \n2.Exit:'))
                        if user==1:
                            print('Home page')
                        else:
                            print('Thank you for visiting')
                else:
                    print('change can not deposit')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
            elif option==3:
                print(f'Your Current Balance:{ICIC_Durga['BALANCE']}')
                print('Transaction History:',ICIC_Durga['Transaction'])
            elif option==4:
                print('Thank you for visiting ICIC')
                break
            else:
                print('Invalid option')      
        else:
            remain_A-=1
            if remain_A>0:
                print(f'incorrect pin and you have only {remain_A}')
            else:
                print('card is block')
                break
    else:
        print('plz enter only 4 digit atm pin')
