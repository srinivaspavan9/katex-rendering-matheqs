from flask import Flask,render_template,request
from sympy.solvers import solve
from sympy import Symbol
from sympy import simplify
import urllib.request,json
app=Flask(__name__)

@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():
    if request.method=='POST':
        ceq=request.form.get('ceq')
        pvar=request.form.get('pvar')
        qvar=request.form.get('qvar')
        file=open("templates/index.html",'w')
        s='''{% extends 'base.html' %}
        {% block body %}</br>
        <h4><b>Problem:</b> </br>Assume that an entrepreneur's 
        short-run total cost function is C='''+ceq+'''
        Determine the output level at which he maximizes profit if p='''+pvar+'''.Compute the
        output elasticity of cost at this output.</h4>
        <h6>Try changing with verified equations and you can still solve the problem.</h6>
        <form action="/index" method="POST">
        <p>C=<input type="text" name="ceq" placeholder="q**3-10*q**2+17*q+66"> p=<input 
        type="text" name="pvar" placeholder="5"> variable in C:<input type="text" name="qvar" placeholder="q">  <input type="submit" class="btn btn-outline-success" value="solve"></p>
        </form>
        <p>Multiplied terms in eqn's such as '17q' should be entered as '17*q'.follow the  proper syntax as shown in the question.</p>
        <p>The variable input field is the variable used in eqn,for this question it's 'q',if the eqn is of form f(x) then it will be 'x'</p>
        <h5><b>Solution:</b></h5>
        <p>The firm produces at MC=P to maximize profit</p>
        <p>MC=marginal cost and P=price</p>
        <p>MC is the change in the total cost and a change in a
        function is found by the first differentiation</p>
        <p>MC=dC/dq=</p>
        '''
        ceq=ceq.replace(' ','')
        tempeq=ceq
        ceq=ceq.replace('+',"%2B")
        url="http://ravigitte.pythonanywhere.com/solve/?exp=diff("+ceq+","+qvar+")"
        res=urllib.request.urlopen(url)
        data=json.loads(res.read())
        eq=None
        for i in range(3):
            if('output' in data[i]):
                s=s+data[i]['output']
            if(i==1 and 'value' in data[i]):
                eq=data[i]['value']
        eq=eq.replace(' ','')
        tempeq2=eq
        q=Symbol(qvar,real=True)
        roots=solve(simplify(eq+"-"+"("+pvar+")"))
        s=s+"<p>MC ="+eq+"</p>"
        s=s+"<p>Equating to P</p>"
        s=s+"<p>"+eq+"="+pvar+"</p>"
        eq=eq.replace('+','%2B')
        eq=eq+"-"+"("+pvar+")"
        url2="http://ravigitte.pythonanywhere.com/solve/?exp=solve("+eq+")"
        res2=urllib.request.urlopen(url2)
        data2=json.loads(res2.read())
        for i in range(len(data2)):
            if('output' in data2[i]):
                s=s+data2[i]['output']
        flag=True
        for i in roots:
            if(i.is_real):
                flag=True
            else:
                flag=False
        if(flag==True):
            s=s+"<p>q>0,the profit is maximum at highest q as MC is increasing</p>"
            s=s+"<p>q="+str(max(roots))+" then MC is increasing and q="+str(min(roots))+"then MC is decreasing so the profit is maximum at q="+str(max(roots))+"</p>"
            s=s+"<p>So the profit is maximum at q="+str(max(roots))+" units.</p>"
            s=s+"<p>=======================================</p>"
            s=s+"<p>Output elasticity formula is:(C/q)*(dq/dC) =</p>"
            # expr=simplify("("+tempeq+"/"+qvar+")*("+"1/"+tempeq2+")")
            try:
                expr1=simplify(tempeq)
                expr2=simplify(qvar)
                expr3=simplify(tempeq2)
            except:
                s=s+"<h1 style='color:red'>Either the equation you entered is not following proper syntax or is invalid</h1>"
                s=s+"<h2 style='color:red'>Please try again</h2>"
                s=s+"{%endblock%}"
                file.write(s)
                file.close()
                return render_template('index.html')
            m=max(roots)
            m=m.evalf()
            print(m)
            expr1=expr1.subs(q,float(m))
            expr2=expr2.subs(q,float(m))
            expr3=expr3.subs(q,float(m))
            expr4=simplify((expr1/expr2)*(1/expr3))
            show=simplify((expr1/expr2)*(1/expr3))
            ans=expr4.subs(qvar,float(m))
            print(ans)
            # ans2=expr4.subs(q,float(m))
            # expr=expr.subs(q,max(roots))
            s=s+"<p> "+str(show)+" = </p>"
            s=s+"<p> The output elasticity is :"+str(ans)+"</p>"
            # s=s+"<h2> = "++"</h2>"
            s=s+'''{%endblock%}'''
            file.write(s)
            file.close()
            return render_template('index.html')
        else:
            s=s+"<h3>The equation :"+tempeq2+" has complex roots</h3>"
            s=s+"<h3>The given equation is unverified/not suitable.</h3>{%endblock%}"
            file.write(s)
            file.close()
            return render_template('index.html')

    else:
        file=open("templates/index.html",'w')
        s='''{% extends 'base.html' %}
        {% block body %}</br>
        <h4><b>Problem:</b> </br>Assume that an entrepreneur's 
        short-run total cost function is C=q**3-10*q**2+17*q+66
        Determine the output level at which he maximizes profit if p=5.Compute the
        output elasticity of cost at this output.</h4>
        <h6>Try changing with verified equations and you can still solve the problem.</h6>
        <form action="/index" method="POST">
        <p>C=<input type="text" name="ceq" placeholder="q**3-10*q**2+17*q+66"> p=<input 
        type="text" name="pvar" placeholder="5"> variable in C:<input type="text" name="qvar" placeholder="q">  <input type="submit" class="btn btn-outline-success" value="solve"></p>
        </form>
        <p>Multiplied terms in eqn's such as '17q' should be entered as '17*q'.follow the  proper syntax as shown in the question.</p>
        <p>The variable input field is the variable used in eqn,for this question it's 'q',if the eqn is of form f(x) then it will be 'x'</p>
        <h5><b>Solution:</b></h5>
        <p>The firm produces at MC=P to maximize profit</p>
        <p>MC=marginal cost and P=price</p>
        <p>MC is the change in the total cost and a change in a
        function is found by the first differentiation</p>
        <p>MC=dC/dq=</p>
        '''
        url="http://ravigitte.pythonanywhere.com/solve/?exp=diff(q**3-10q**2%2B17q%2B66,q)"
        res=urllib.request.urlopen(url)
        data=json.loads(res.read())
        eq=None
        for i in range(3):
            if('output' in data[i]):
                s=s+data[i]['output']
            if(i==1 and 'value' in data[i]):
                eq=data[i]['value']
        eq=eq.replace(' ','')
        q=Symbol('q')
        roots=solve(eq+"-5")
        s=s+"<p>MC ="+eq+"</p>"
        s=s+"<p>Equating to P</p>"
        s=s+"<p>"+eq+"=5</p>"
        eq=eq.replace('+','%2B')
        eq=eq+"-"+"5"
        url2="http://ravigitte.pythonanywhere.com/solve/?exp=solve("+eq+")"
        res2=urllib.request.urlopen(url2)
        data2=json.loads(res2.read())
        for i in range(len(data2)):
            if('output' in data2[i]):
                s=s+data2[i]['output']
        s=s+"<p>q>0,the profit is maximum at highest q as MC is increasing</p>"
        s=s+"<p>q="+str(max(roots))+" then MC is increasing and q="+str(min(roots))+"then MC is decreasing so the profit is maximum at q=6</p>"
        s=s+"<p>So the profit is maximum at q=6 units.</p>"
        s=s+"<p>=======================================</p>"
        s=s+"<p>Output elasticity formula is:(C/q)*(dq/dC)=</p>"
        s=s+"<p>((q**3-10q**2+17q+66)/q)*(1/3q**2-20q+17)</p>"
        s=s+"<p>=24/6*1/5</p>"
        s=s+"<p>=0.8</p>"
        s=s+"<p>The output elasticity is 0.8</p>"
        s=s+'''{%endblock%}'''
        file.write(s)
        file.close()
        return render_template('index.html')

@app.route('/base')
def base():
  return render_template('base.html')

if __name__=='__main__':
    app.run(debug=True)