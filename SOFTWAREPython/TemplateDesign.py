import datetime
from faker import Faker


# lambda function that can create fake data
fakeText = lambda lenght: Faker().text(lenght)

# Template pattern implemented in python
class PrepareReport:
    global date_formatted
    date = datetime.datetime.now()
    date_formatted = date.strftime('%d-%m-%Y')

    def title(self):pass
    def body(self):pass
    def footer(self):pass

    #drive function to call all the other functions
    def prepare(self,Title='Default',Date=date_formatted,SubTitle='Default',
    Content='Default',Name='Default',Surname='Default',City='',Country=''):
        self.title(Title,Date)
        self.body(SubTitle,Content)
        self.footer(Name,Surname,City,Country)

#sub classes
class to_html(PrepareReport):
    def title(self,Title='Default',Date=datetime.datetime.now()):
        with open('report.html','w') as f:
            f.write(f"""<html>
    <head>
        <title>{Title}</title>
    </head>
    <body>
        <div style='display:flex;justify-content:space-between;align-items:center' class='report-header'>
            <h1>{Title}</h1>
            <h3>{Date}</h3>
        </div>
        <hr>

        <!--<p>Content will be added from another function</p>-->
            """)
        return print('Report head created')
    def body(self,SubTitle='Default',Content='Default'):
        with open('report.html','a') as f:
            f.write(f"""
        <div class='content' style='width:50%;margin:0 auto;text-align:center;margin-top:5rem;'>
            <h2>{SubTitle}</h2>
            <p>{Content}</p>
        </div>
        <!-- Footer will be added by another function -->
            """)
        return print('Report body created')
    def footer(self,Name='Presenter',Surname='Surname',City='None',Country='None'):
        with open('report.html','a') as f:
            f.write(f"""
        <footer>
        <center><h3>{Name} {Surname} {City}/{Country}</h3></center>
        </footer>
    </body>
</html>
            """)
        return print('Report footer created')
    
class to_txt(PrepareReport):
    #overriding the title function
    def title(self,title='Default',date=datetime.datetime.now()):
        with open('report.txt','w') as f:
            f.write(f"""
{title}
{date}
--------------------------------------------------------------------------------
            """)
        return print('Report head created')
    #overriding the body function
    def body(self,SubTitle='Default',Content='Default'):
        with open('report.txt','a') as f:
            f.write(f"""
{SubTitle}
{Content}
--------------------------------------------------------------------------------

            """)
        return print('Report body created')
    #overriding the footer function
    def footer(self,Name='Presenter',Surname='Surname',City='None',Country='None'):
        with open('report.txt','a') as f:
            f.write(f"""
{Name} {Surname} {City}/{Country}
            """)
        return print('Report has been created in report.txt')
    

#fakeText(lenght) enter the number of characters you want to generate
#report will be deciding the method
report = to_txt()
#calling the prepare function from skeleton class
report.prepare('Alien Invasion',date_formatted,'Alien Invasion on Earth!',
fakeText(1000),'Atakan','Yildirim','Izmir','Turkey')
