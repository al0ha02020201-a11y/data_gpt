def ask_question(question_number, question_text, options, correct_answer):
    print(f"\nВопрос {question_number}: {question_text}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    user_answer = input("Ваш ответ (номер): ").strip()
    return user_answer == str(correct_answer)


def main():
    quiz_questions = [
        (
            "Какая профессия в наборе practice чаще связана с увлечением 'кодинг'?",
            ["Учитель", "Разработчик", "Врач", "Маркетолог"],
            2,
        ),
        (
            "В наборе practice какое увлечение чаще встречается у дизайнеров?",
            ["Фотография", "Садоводство", "Шахматы", "Путешествия"],
            1,
        ),
        (
            "В наборе tests какая профессия чаще связана с увлечением 'рисование'?",
            ["Архитектор", "Юрист", "Логист", "Финансист"],
            1,
        ),
        (
            "В наборе tests какая профессия чаще связана с увлечением 'чтение'?",
            ["Биолог", "Психолог", "Менеджер проектов", "Логист"],
            2,
        ),
        (
            "В каком наборе ярче выражена зависимость между техпрофессиями и 'кодингом'?",
            ["practice", "tests"],
            1,
        ),
    ]

    correct_answers_count = 0
    for index, (question_text, options, correct_answer) in enumerate(quiz_questions, 1):
        if ask_question(index, question_text, options, correct_answer):
            print("Верно!")
            correct_answers_count += 1
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}.")

    print(f"\nВаш результат: {correct_answers_count} из {len(quiz_questions)}")


if __name__ == "__main__":
    main()
