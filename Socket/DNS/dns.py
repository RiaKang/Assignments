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

    #domain 정보 삭제하기
    def delete_domain(self, ip:str, dname:str):
        self.cur.execute(f"DELETE FROM domains WHERE ip = ? AND dname = ?", (ip, dname))
        self.con.commit()

    #Domain 이름을 받아서 ip주소 찾기
    def search_domain_ip(self, dname:str):
        self.cur.execute(f"SELECT ip FROM domains WHERE dname = ?", (dname,))
        ip_list = self.cur.fetchall()
        for ip in ip_list:
            print(ip)
        
    #ip주소를 받아서 도메인 이름 찾기
    def search_domain_dname(self, ip:str):
        self.cur.execute(f"SELECT dname FROM domains WHERE ip = ?", (ip,))
        dname_list = self.cur.fetchall()
        for dname in dname_list:
            print(dname)

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
    
    try:
        dns.delete_domain('20.200.245.247', 'github.com')
        dns.search_domain_ip('dankook.ac.kr')
        dns.search_domain_dname('142.250.204.46')
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

    for row in dns.cur.execute("""SELECT * FROM domains"""):
        print(row)
