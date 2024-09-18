import os
import secrets
from flask import render_template,flash,redirect,url_for, flash, request, abort
from flask_1.models import User,Post
from flask_1 import app,db,bcrypt
from flask_1.forms import RegistrationForm,LoginForm, UpdateAccountForm, PostForm
from flask_login import login_user,current_user, logout_user, login_required


data=[{"content":'''What Is a Bank?
A bank is a financial institution that is licensed to accept checking and savings deposits and make loans. Banks also provide related services such as individual retirement accounts (IRAs), certificates of deposit (CDs), currency exchange, personal loans, and safe deposit boxes.

There are several types of banks including retail banks, commercial or corporate banks, and investment banks.

In the U.S., banks are regulated by the national government and by the individual states.

Key Takeaways
A bank is a financial institution licensed to receive deposits and make loans.
There are several types of banks including retail, commercial, and investment banks.
In most countries, banks are regulated by the national government or central bank.
Understanding Banks
Banks have existed since at least the 14th century. They provide a safe place for consumers and business owners to stow their cash and a source of loans for personal purchases and business ventures. In turn, the banks use the cash that is deposited to make loans and collect interest on them.

The basic business plan hasn't changed much since the Medici family started dabbling in banking during the Renaissance, but the range of products that banks offer has grown.

Basic Bank Services
Banks offer various ways to stash your cash and various ways to borrow money.

Checking Accounts

Checking accounts are deposits used by consumers and businesses to pay their bills and make cash withdrawals. They pay little or no interest and typically come with monthly fees, usage fees, or both.

Today's consumers generally have their paychecks and any other regular payments automatically deposited in one of these accounts.


Savings Accounts

Savings accounts pay interest to the depositor. Depending on how long account holders hope to keep their money in the bank, they can open a regular savings account that pays a little interest or a certificate of deposit (CD) that pays a little more interest. The CDs can earn interest for as little as a few months or as long as five years or more.

It is important to note that the money in checking accounts, savings accounts, and CDs is insured up to a maximum of $250,000 by the federal government through the Federal Deposit Insurance Corp. (FDIC).
1

Loan Services
Banks make loans to consumers and businesses. The cash that is deposited by their customers is lent out to other customers at a higher rate of interest than the depositor is paid.

At the highest level, this is the process that keeps the economy humming. People deposit their money in banks; the bank lends the money out in car loans, credit cards, mortgages, and business loans. The loan recipients spend the money they borrow, the bank earns interest on the loans, and the process keeps money moving through the system.

Just like any other business, the goal of a bank is to earn a profit for its owners. For most banks, the owners are their shareholders. Banks do this by charging more interest on the loans and other debt they issue to borrowers than they pay to people who use their savings vehicles.

For example, a bank may pay 1% interest on savings accounts and charge 6% interest for its mortgage loans, earning a gross profit of 5% for its owners.

Banks make a profit by charging more interest for loans than they pay on savings accounts.
Brick-and-Mortar and Online Banks
Banks range in size from small, community-based institutions to global commercial banks.

According to the FDIC, there were just over 4,200 FDIC-insured commercial banks in the United States as of 2021.
2
 This number includes national banks, state-chartered banks, commercial banks, and other financial institutions.

Traditional banks now offer both brick-and-mortar branch locations and online services. Online-only banks began emerging in early 2010s.

Consumers choose a bank based on its interest rates, the fees it charges, and the convenience of its locations, among other factors.

How Banking Works
Investopedia / Theresa Chiechi

How Are Banks Regulated?
U.S. banks came under intense scrutiny after the global financial crisis of 2008. The regulatory environment for banks was tightened considerably as a result.

Depending on their business structures, U.S. banks may be regulated at the state or national level, or both. State banks are regulated by each state's department of banking or department of financial institutions. This agency is generally responsible for issues such as permitted practices, how much interest a bank can charge, and auditing and inspecting banks.

National banks are regulated by the Office of the Comptroller of the Currency (OCC). OCC regulations primarily cover bank capital levels, asset quality, and liquidity. As noted above, banks with FDIC insurance are also regulated by the FDIC.

The Dodd-Frank Wall Street Reform and Consumer Protection Act was passed in 2010 following the financial crisis with the intention of reducing risks in the U.S. financial system. Under this act, large banks now have to submit to regular tests that measure whether they have sufficient capital to continue operating under challenging economic conditions. This annual assessment is referred to as a stress test.
3

Types of Banks
Most banks can be categorized as retail, commercial or corporate, or investment banks. The big global banks often operate separate arms for each of these categories.

Retail Banks
Retail banks offer their services to the general public and usually have branch offices as well as main offices for the convenience of their customers.

They provide a range of services such as checking and savings accounts, loan and mortgage services, financing for automobiles, and short-term loans such as overdraft protection. Many also offer credit cards.

They also offer access to investments in CDs, mutual funds, and individual retirement accounts (IRAs). The larger retail banks also cater to high-net-worth individuals with specialty services such as private banking and wealth management services.

Examples of retail banks include TD Bank and Citibank.

Commercial or Corporate Banks
Commercial or corporate banks tailor their services to business clients, from small business owners to large, corporate entities. Along with day-to-day business banking, these banks also offer credit services, cash management, commercial real estate services, employer services, and trade finance,

JPMorgan Chase and Bank of America are examples of commercial banks, though both have large retail banking divisions as well.

Investment Banks
Investment banks focus on providing corporate clients with complex services and financial transactions such as underwriting and assisting with merger and acquisition (M&A) activity. They are primarily financial intermediaries in these transactions.

Their clients include large corporations, other financial institutions, pension funds, governments, and hedge funds.

Morgan Stanley and Goldman Sachs are among the biggest U.S. investment banks.

Central Banks
Unlike the banks above, central banks does not deal directly with the public. A central bank is an independent institution authorized by a government to oversee the nation's money supply and its monetary policy.

As such, central banks are responsible for the stability of the currency and of the economic system as a whole. They also have a role in regulating the capital and reserve requirements of the nation's banks.

The U.S. Federal Reserve Bank is the central bank of the U.S. The European Central Bank, the Bank of England, the Bank of Japan, the Swiss National Bank, and the People’s Bank of China are among its counterparts in other nations.

Bank vs. Credit Union
Credit unions offer banking services but, unlike banks, they are not-for-profit institutions created for and managed by their members or customers. Credit unions provide routine banking services to their clients, who are generally called members.

Credit unions are created, owned, and operated by their clients, and are generally tax-exempt. Members purchase shares in the co-op, and that money is pooled together to fund the credit union's loans.

They tend to provide a limited range of services compared to banks. They also have fewer locations and automated teller machines (ATMs).

How Do I Know My Money Is Safe in a Bank?
The Federal Deposit Insurance Corporation (FDIC) is an independent agency created by Congress to maintain stability and public confidence in the U.S. financial system. The FDIC supervises and examines banks to ensure that the money they handle is safe.

Moreover, it insures your money. The insurance maximum is $250,000 per depositor, per insured bank, for each account ownership category.

You don't have to purchase this insurance. If you open a deposit in an FDIC-insured bank, you are automatically covered.

The agency's BankFind site can help you identify FDIC-insured banks and branches.

Are Any Non-Bank Accounts Insured?
The mission of the Securities Investor Protection Corporation (SIPC) is to recover cash and securities in the event a member brokerage firm fails. SIPC is a nonprofit corporation that Congress created in 1970. SIPC protects the customers of all registered brokerage firms in the U.S. This applies to stocks and bonds (securities) and cash that a brokerage firm holds. Brokerage firms rarely fail or close suddenly, but if this occurs, the SIPC helps close the firm through liquidation and establishes claims processes by which it can protect the investor. SIPC protects your account for up to $500,000 in securities. This includes a limit of $250,000 in cash in your account. This link will show you a list of all registered SIPC members.

Should I Choose a Retail Bank, Credit Union, or Commercial Bank?
You should consider whether you want to keep both business and personal accounts at the same bank, or whether you want them at separate banks. A retail bank, which has basic banking services for customers, is the most appropriate for everyday banking. You can choose a traditional bank, which has a physical building, or an online bank if you don't want or need to physically visit a bank branch. You might consider a credit union, which is a nonprofit institution and is available to serve the needs of people with a common employer, labor union, or professional interest.

What Other Factors Go Into Choosing a Bank?
Bank size is another consideration. Large retail banks are often well-known, big-name banks and have locations throughout the U.S., which is convenient if you travel often for work or vacation. You would have easier access to your funds when you're away and may be able to avoid foreign ATM fees.

Otherwise, you might find that a smaller bank would offer more personalized customer service and the products you prefer. A community bank, for example, takes deposits and lends locally, which could offer a more personalized banking relationship.

Choose a convenient location if you are choosing a bank with a brick-and-mortar location. If you have a financial emergency, you don't want to have to travel a long distance to get cash.

See if the bank you are choosing offers other services such as credit cards, loans, and safe deposit boxes. Some banks also offer smartphone apps, which can be useful.

Check the fees associated with the accounts you want to open. Banks charge interest on loans as well as monthly maintenance fees, overdraft fees, and wire transfer fees. Some large banks are moving to end overdraft fees in 2022, so that could be an important consideration.
4

The Bottom Line
At the very least, a bank is where you stash your cash until you use it to pay the bills or withdraw money. It can also be the place where you get a loan to buy a car or a mortgage to buy a house. If you're running a small business, it may be where you go to borrow money to expand or improve.

Before choosing a bank, you should make a comparison of the various fees and charges that come with your accounts or any loans you might need. A bit of research and comparison will ensure you find the right fit for safeguarding your money, establishing credit, making payments, applying for loans, receiving funds, and saving money for future needs such as retirement, emergencies, and homebuying.'''},
]
       

import requests
import json

posts = []
r = requests.get("https://api.thingspeak.com/channels/2567333/feeds.json?api_key=T1YTUYGYW4TUOLM4&results=100")
n = json.loads(r.text)

num = 0
for i in range(len(n["feeds"])):
    disease = []
    list1 = [n["feeds"][i]["entry_id"], n['feeds'][i]['field1'], n['feeds'][i]['field2'], n['feeds'][i]['field3'], n['feeds'][i]['created_at']]
    num += 1
    if num!=1 :  # If it's not the first iteration
        if list1[1] == "1":
            disease.append("ppr")
        if list1[2] == "1":
            disease.append("anthrax")
        if list1[3] == "1":
            disease.append("tetanus")
        disease_str = ", ".join(disease) if disease else "none"
        dict1 = {
            "author": list1[0]-1,
            "title": "disease detected on " + list1[4],
            "content": "The diseases detected is/are " + disease_str,
            "date": list1[4]
        }
        posts.append(dict1)


print(posts)
@app.route("/")
def home():
    return render_template('home.html',posts=posts,title="home sweet home") #we will have access to this variable in the template

@app.route("/about")
def about():
    return render_template("about.html",posts=data)

@app.route("/register",methods=['POST','GET']) #list of allowed methods in our route
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    #creating instance of the registration form
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}','success') #easy to send ot alert , category
        return redirect(url_for('home'));
    return render_template("register_1.html",title='Register',form=form)
# just like how we set posts , we have access to this instance form in the register template for showing the data

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        #if form.email.data=="admin@gmail.com" and form.password.data=="hello":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
                '''flash("You have successfully logged in","success")
                return redirect(url_for('home'))'''
        else:
            flash("Login unsuccessful please check your password")
    return render_template("login.html",title='Login',form=form)
@app.route("/post/new", methods=['GET', 'POST'])
#@login_required

def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/chatbot")
def chatbot():
    render_template("chatbot.html")


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

'''def new_post():
    return render_template('create_post.html',title='New Post')'''