import sqlite3
import random

# Tạo cơ sở dữ liệu SQLite
def init_db():
    conn = sqlite3.connect("tarot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarot_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT UNIQUE,
            card TEXT,
            meaning TEXT
        )
    """)
    conn.commit()
    conn.close()

# Truy vấn cơ sở dữ liệu
def query_database(question):
    conn = sqlite3.connect("tarot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT card, meaning FROM tarot_data WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    return result if result else None

# Chọn ngẫu nhiên một lá bài Tarot
def draw_tarot_card():
    cards = [
        ("The Fool", "A new beginning, innocence, spontaneity, a free spirit."),
        ("The Magician", "Power, skill, concentration, action, resourcefulness."),
        ("The High Priestess", "Intuition, unconscious knowledge, wisdom, secrets."),
        ("The Empress", "Fertility, beauty, nature, abundance, nurturing."),
        ("The Emperor", "Authority, structure, control, fatherhood, leadership."),
        ("The Hierophant", "Tradition, conformity, spirituality, religion, community."),
        ("The Lovers", "Love, union, partnership, choices, harmony."),
        ("The Chariot", "Victory, control, determination, willpower, action."),
        ("Strength", "Courage, patience, inner strength, compassion, confidence."),
        ("The Hermit", "Soul searching, introspection, solitude, guidance."),
        ("Wheel of Fortune", "Luck, destiny, karma, change, cycles."),
        ("Justice", "Fairness, truth, law, balance, accountability."),
        ("The Hanged Man", "Sacrifice, release, surrender, new perspectives."),
        ("Death", "Endings, transformation, change, transition, rebirth."),
        ("Temperance", "Balance, moderation, patience, purpose, harmony."),
        ("The Devil", "Temptation, materialism, addiction, bondage, restriction."),
        ("The Tower", "Sudden upheaval, chaos, revelation, destruction."),
        ("The Star", "Hope, inspiration, renewal, spirituality, guidance."),
        ("The Moon", "Illusion, intuition, dreams, fear, the unconscious."),
        ("The Sun", "Success, vitality, joy, abundance, enlightenment."),
        ("Judgement", "Judgment, rebirth, inner calling, reflection."),
        ("The World", "Completion, accomplishment, wholeness, fulfillment."),
    ]
    # Chọn ngẫu nhiên một lá bài
    card = random.choice(cards)
    return card

# Chèn dữ liệu mẫu vào cơ sở dữ liệu
def insert_sample_data():
    conn = sqlite3.connect("tarot.db")
    cursor = conn.cursor()
    sample_data = [
        ("Tình yêu của tôi sẽ như thế nào?", "The Lovers", "Love, union, partnership, choices, harmony."),
        ("Tôi nên làm gì để cải thiện công việc?", "The Chariot", "Victory, control, determination, willpower, action."),
        ("Tình hình tài chính của tôi sẽ ra sao?", "The Emperor", "Authority, structure, control, fatherhood, leadership."),
    ]
    cursor.executemany("INSERT OR IGNORE INTO tarot_data (question, card, meaning) VALUES (?, ?, ?)", sample_data)
    conn.commit()
    conn.close()

# Hàm chính cho chatbot
def main():
    init_db()
    insert_sample_data()
    print("Chào bạn! Tôi là chatbot tư vấn bài Tarot. Hãy hỏi tôi một câu hỏi và tôi sẽ rút bài cho bạn.")
    print("Gõ 'exit' để thoát.")
    
    while True:
        question = input("Bạn: ").strip()
        if question.lower() == "exit":
            break
        
        # Kiểm tra trong cơ sở dữ liệu nếu có câu trả lời cho câu hỏi này
        answer = query_database(question)
        
        # Nếu không có câu trả lời trong cơ sở dữ liệu, rút ngẫu nhiên một lá bài
        if not answer:
            card, meaning = draw_tarot_card()
            answer = (card, meaning)
        
        print(f"Bot: Bạn đã rút được lá bài {answer[0]}.\nÝ nghĩa: {answer[1]}")

if __name__ == "__main__":
    main()
