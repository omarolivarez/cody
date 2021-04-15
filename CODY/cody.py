import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style
from tkinter import scrolledtext

class Cody(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        rl = 1
        rw = 2
        rl2 = 3
        rw2 = 4
        
        
        # this section sets which columns are the ones that move - weight is what will expand when expanded
        self.pack(fill=BOTH, expand=True)
        self.rowconfigure(5, pad=7)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        
        #lbl = Label(self, text="Windows")
        #lbl.grid(sticky=W, pady=4, padx=5)
        select_btn = Button(self, text="Select CSV",command=self.import_csv_data)
        select_btn.grid(sticky=E, pady=12, padx=5, columnspan = 10, rowspan=1) #
        
        # white text area
        #area = Text(self)
        #area.grid(row=1, column=0, columnspan=3, rowspan=4, padx=5, sticky=N+S+E+W) 
        text_area = scrolledtext.ScrolledText(self, wrap = tkinter.WORD, 
                                      width = 40, padx = 2, height = 10, 
                                      font = ("Times New Roman", 12))
        text_area.insert(INSERT, ">these statues would fit in nicely. In addition to being mostly unremarkable, a lot of these statues are huge. It's one thing to preserve a massive sculpture of beautiful or impactful art. But in terms of presenting the history or oppression, these statues seem like a massive waste of space. I don't know I've ever been to a museum that addresses the Civil Rights movement and seen a place where Charlottesville's Lee statue, for example, would actually be worth it's real estate. The civil rights museum in Atlanta has a huge number of exhibits that are more powerful and better uses of space.\n \
___The National Center for Civil and Human Rights in Atlanta is an amazing experience. There should be more museums like it across the country. When I visited, it was very hard for me to imagine where a statue could positively contribute to their effort as a museum. The statues are so very large and... mostly unremarkable. Police used attack dogs and fire hoses on peaceful marches, and MLK was one of the most hated public figures in his time. Projecting news reels on a wall was much more powerful than the enormous space Charlottesville's very boring Lee statue would take up. Maybe a couple should be preserved with plenty of context, but there are hundreds and they are not that interesting. I don't think it's worth any more public money than it takes to dismantle and remove them.\n \
___>let people forget. This is part of why I don't really want them in museums. Maybe one or two. But not the dozens or hundreds that are out there. They're big, boring, and what they're intended to remind is the glory of the Confederacy, not the people it fought to oppress. The Civil Rights museum in Atlanta is amazing. They can remind people how much MLK was hated and how oppressed people were with video reels and news clips, let alone the other creative installations they have. I absolutely can't imagine where one of these massive statues would be a responsible use of space. I think 'put them in museums' is a fallback for the people who want to preserve them. Keep them up in public if you can. But if not, make removing them complicated and costly by forcing people to find a museum that will take and display them. And how many of those will be private museums that don't give proper context, and just display a massive statue glorifying the confederacy? Holocaust museums rightly don't have massive sculptures to the glory of the Nazi party or Hitler. It's absolutely the wrong thing to focus on preserving.\n \
___There seems an obvious difference people miss when they compare these statues to great works of art. These statues *are not* great works of art. They're just statues meant to honor someone. Similarly, the myriad of Confederate statues in America are of little to no artistic value. They're not interesting at all. Like you mention, great works of art get preserved all the time despite their questionable morals. Because they're great works of art. They have value beyond their questionable morals.\n \
 ___I'm not going to tell you how to value MLK, but that's kind of the opposite of what I argued. He was a massive activist for achieving racial equality. He had much less influential views on homosexuality. So I think it ends up being fine to celebrate his racial justice achievements while acknowledging he was wrong on homosexuality. In a world where MLKs views on homosexuality were as massively influential as his racial views, I think we'd have a much bigger obligation to contextualize the celebrations of his racial justice work. Edit: Compared to someone who became wealthy off of enslaving and buying and selling people who then gave *some* of that money to philanthropy, or to, for example, Robert E. Lee who was a good general for a war to preserve slavery? I think the case of MLK's racial justice work and his other shitty views is both obviously and enormously different.\n \
___I think the same rubric applies. His views on homosexuality were largely separable from his efforts at racial justice. You can praise one while condemning the other. They don't seem exceptionally mixed to me. His work on racial justice vastly eclipses his views on homosexuality. He was a key leader advocating the equal treatment of races. He had less influential views about gay rights. So you can celebrate his racial justice work without being overwhelmed by his views of homosexuality. Like every historical figure, he had shitty sides to him that should be addressed and discussed. It's quite possible he was also an abusive womanizer. Which is terrible. But again separable from his racial justice work and not eclipsing it.\n \
___Also not an expert, but AFAIK a lot of Washington's clout and wealth came from his wife's massive plantation. His military status is much more important, but I think he was still the wealthy, plantation and slave owning class. Would he be put in a position to lead the military without that? I'm unsure. From what I see Jefforson inherited his large plantation also quite young. And his intellectual ambitions were backed by the fact he was also the wealthy plantation and slave owning class. I don't mean to say they were fabulously wealthy. But I think a lot of the other things they were known for were allowed by being part of the land and many many slave owning 'much better off than the average joe' class.\n \
___Sure, but the transparency is important. Directly profiting from slave trade or owning slaves is different from the person who can't buy food without buying it from a plantation run forced slave labor. And it's different from a person who's wealth is tied into the institution of slavery in complicated ways. This comes back to my point of separability. For the vast majority of things we can see a good as separate from a bad. This issue of philanthropy is a bit weird because the 'good' is often tied to someone having immense wealth they got from somewhere. Joe Schmoe who got his house and job and security in a complicated relationship with global economic abuses but then also tries to do some good for his community? They're both important issues, but I think one can be celebrated and the other denounced without having to overly cross them. Maybe several decades from now that won't be true. Or for some people it's not true today. And we'll see what I call a 'complicated relationship' as clear exploitation that eclipses donating to big brothers big sisters. Then I won't begrudge people for not wanting to celebrate, because celebrating will be sending a different message.\n \
___Broadly, I don't think you should celebrate someone as a great philanthropist if their money is ill-gotten. I think the directness of the slave trade makes it a bit different. There is no ambiguity that it is atrocious and the people knew what they were doing even if they didn't acknowledge it as evil. There are a lot of ways to get wealthy that aren't so directly exploitative and cruel. That said.. By and large, I don't think it's a good trade to let people who get wealthy exploiting others buy their names back with a pittance of philanthropic activity. You'd have to give me a more specific example before I make a more specific argument. Local hotel chain owner who tries to give back to their community? Sure. Bezos who builds wealth by exploiting horrible warehouse conditions? His labor practices will be front and center over any small philanthropy until they're reformed. Ford who had a pretty socialist view of his labor force, tried to do some good with his wealth, and was also a rabid anti-semite. We get into separability and eclipsing issues.\n \
___I think the rubric still fits. And also captures how celebrating them is becoming more questionable. Washington and Jefferson are celebrated for the founding of the country. This is often seen as separable from the issues of their slave ownership. You can celebrate one while condemning the other. The founding of what's now the most powerful country in the world is thought of as a massive thing. Their ownership and profiting off of hundreds of slaves is terrible, but it's hard to say it eclipses forming the country. Where it gets dicey is when you question if these things really are separable. There are controversial takes that the country was founded primarily to benefit these big land holders financially. And Washington and Jefferson made their financial wealth by forcing slaves to labor and stealing the products of that labor. It's also worth questioning if slavery would have ended earlier in America if we hadn't revolted and formed a country with a massive economic dependence on it. And further, the founding and early years of the country very much have slavery as an issue front and center. So aught we celebrate people who founded a country with such an integrated horrific abuse? I understand how people are unforgiving that they achieved and maintained their wealth and influence on the backs of slaves, and made a country deeply intertwined with slavery. I can see how people view this as inseparable and possibly even eclipsing of what we celebrate them for. I especially sympathize with people who are viscerally reminded that the heroes we hold up as founding a nation with 'liberty and justice for all' saw them as sub humans who would be property for a century. Long story short, if you're asking me personally, I think celebrating their contributions is fine if we also provide context for their abuses. But I also think my opinion is less important the the opinions of communities they thought were subhuman and were abused by the country they founded.\n \
___The statue exist today for the people who see it today. The values it represents have to have meaning for the people seeing it today. To counter your Hitler, what if there was a man cheered by his community for driving all the jews from his city? Even the king and catholic church said this was a noble thing? Should the statue be kept because the people of his time thought he was good? The statue exists today still because we still see philanthropy as good. But we're increasingly seeing the slave trade as horrific. When I see stuff like this, I ask: 1) Is the terrible thing separable from the good thing? We can celebrate a mathematical achievement even if the mathematician turned out to be a bad person. 2) Does the terrible thing overshadow the good thing? It's hard to celebrate the math if everyone's first thought is 'that mathematician murdered all those children.' I think he fails both. His philanthropy and his slave trade are not unrelated things. He became wealthy trading slaves, and used some of that money for philanthropy. A completley horrific treatment of other human beings. They really are not separable. His slave trade far eclipses his philanthropy. He made life for people at home marginally better using *some* of the funds he gained committing completely atrocious treatment of people. People looking at the statue can't *not* see a slave trader who also did some good philanthropy.")
        text_area.grid(row = 1, column = 0, columnspan=3, rowspan=4, pady = 10, padx = 10, sticky=N+S+E+W)
        
        # input fields
        sl = Label(self, text = "Sex")
        sl.grid(row = rl, column = 10, padx = 5) # 
        self.s = Entry(self)
        self.s.grid(row=rw, column=10, padx = 5)
        
        race_l = Label(self, text = "Race")
        race_l.grid(row = rl, column = 20, padx = 5)
        self.race = Entry(self)
        self.race.grid(row=rw, column=20, padx = 5)
        
        age_l = Label(self, text = "Age")
        age_l.grid(row = rl, column = 30, padx = 5)
        self.age = Entry(self)
        self.age.grid(row=rw, column=30, padx = 5)
        
        region_l = Label(self, text = "Region of Origin")
        region_l.grid(row = rl, column = 40, padx = 5)
        self.region = Entry(self)
        self.region.grid(row=rw, column=40, padx = 5)
        
        blm_l = Label(self, text = "BLM Reference")
        blm_l.grid(row = rl2, column = 10, padx = 5)
        self.blm = Entry(self)
        self.blm.grid(row=rw2, column=10, padx = 5)
        
        viewpoint_l = Label(self, text = "Viewpoint")
        viewpoint_l.grid(row = rl2, column = 20, padx = 5)
        self.viewpoint = Entry(self)
        self.viewpoint.grid(row=rw2, column=20, padx = 5)
        
        style_l = Label(self, text = "Language Style")
        style_l.grid(row = rl2, column = 30, padx = 5)
        self.style = Entry(self)
        self.style.grid(row=rw2, column=30, padx = 5)
        
        abtn = Button(self, text="Next row", command=self.clear_text)
        abtn.grid(row=5, column=10)
       
        
        # Import button
        #import_label = Label(self, text = "Import Data", font = ('bold', 14), pady = 20, padx = 20)
        #import_label.grid(row = 30, column = 10)
        
        #import_button = Button(self, text='Select CSV file',command=self.import_csv_data)
        #import_button.grid(row=30, column=11)
        
        # this code chunk will create a button to close the entire app
        #close_button = Button(app, text='Close',command=app.destroy)
        #close_button.grid(row=30, column=15)
        
        ## MAKING THE INPUT FIELDS
        #input fields row number
        
    def import_csv_data(self):
        #global v
        csv_file_path = askopenfilename()
        print(csv_file_path)
        #v.set(csv_file_path)
        df = pd.read_csv(csv_file_path)
        #print(head(df))
        
    def clear_text(self):
        self.s.delete(0, END)
        self.race.delete(0, END)
        self.age.delete(0, END)
        self.region.delete(0, END)
        self.blm.delete(0, END)
        self.viewpoint.delete(0, END)
        self.style.delete(0, END)

def main():
    # Create window object
    root = Tk()
    root.title("Cody")
    root.geometry('1250x750') # width x height
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()