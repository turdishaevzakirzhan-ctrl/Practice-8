from connect import connect


def main():
    conn = connect()
    cur = conn.cursor()

    
    cur.execute("CALL upsert_contact(%s, %s)", ("Ali", "87001112233"))
    conn.commit()

    
    cur.execute("SELECT * FROM search_contacts(%s)", ("Ali",))
    print("Search:", cur.fetchall())

    
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
    print("Page:", cur.fetchall())

    
    cur.execute("""
        CALL bulk_insert_contacts(
            ARRAY['Aruzhan', 'Nurlan'],
            ARRAY['87009998877', 'wrong_phone']
        )
    """)
    conn.commit()

    
    cur.execute("CALL delete_contact(%s)", ("Ali",))
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()