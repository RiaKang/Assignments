import sqlite3

class DNS():
    def __init__(self) -> None:
        self.con = sqlite3.connect('dns.db')
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS domains (ip text PRIMARY KEY, dname text UNIQUE)
        """)

    def insert_domain(self, ip: str, dname: str):
        self.cur.execute(f"INSERT INTO domains VALUES (?, ?)", (ip, dname))
        self.con.commit()

    def delete_domain(self, ip:str, dname:str):
        self.cur.execute(f"DELETE FROM domains WHERE ip = ? AND dname = ?", (ip, dname))
        self.con.commit()

    #Domain이름을 받아서 ip주소 찾기
    def search_domain_ip(self, dname:str):
        self.cur.execute(f"SELECT * FROM domains WHERE dname = ?", (dname,))
        self.con.commit()
        
    #ip주소를 받아서 도메인 이름 찾기
    def search_domain_dname(self, ip:str):
        self.cur.execute(f"SELECT dname FROM domains WHERE dname = ?", (ip,))
        self.con.commit()

if __name__ == "__main__":
    dns = DNS()
    try:
        dns.insert_domain('20.200.245.247', 'github.com')
        dns.insert_domain('220.69.176.13', 'dankook.ac.kr')
        dns.insert_domain('223.130.195.95', 'www.naver.com')
        dns.insert_domain('142.250.204.46', 'www.google.com')
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

    for row in dns.cur.execute("""SELECT * FROM domains"""):
        print(row)
    
    #delete, search 실험
    #delete 정상 작동, search는 해당 주소 출력이 아직 안됩니다
    try:
        dns.delete_domain('20.200.245.247', 'github.com')
        dns.search_domain_dname('dankook.ac.kr')
        dns.search_domain_ip('142.250.204.46')
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

    for row in dns.cur.execute("""SELECT * FROM domains"""):
        print(row)

    dns.cur.close()
    dns.con.close()
