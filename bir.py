def cash_machine(L1, L2):
    results = [3, 3]
    for action1, action2 in zip(L1, L2):
        if action1 == "share" and action2 == "share":
            results[0] += 2
            results[1] += 2
        elif action1 == "share" and action2 == "steal":
            results[0] += 0
            results[1] += 3
        elif action1 == "steal" and action2 == "share":
            results[0] += 3
            results[1] += 0
        elif action1 == "steal" and action2 == "steal":
            results[0] += 1
            results[1] += 1
    return results

L1 = input("Birinchi odamning harakatlarini kiriting (share/steal): ").strip().split(',')
L2 = input("Ikkinchi odamning harakatlarini kiriting (share/steal): ").strip().split(',')

if len(L1) != len(L2):
    print("Xato: Ikkala odamning harakatlar soni teng bo‘lishi kerak!")
elif any(action not in ["share", "steal"] for action in L1 + L2):
    print("Xato: Faqat 'share' yoki 'steal' kiritilishi mumkin!")
else:
    output = cash_machine(L1, L2)
    print(output)
