from pyquery import PyQuery as pq

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0" id="tony"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''
doc = pq(html)
ul = doc("ul")
li = ul.find("#tony a").remove()
print(li.text())

'''
ul.css("color","green")
print(ul.parents().html())
ul.attr("height","18px")
print(ul.parents().html())
ul.add_class("list")
print(ul.parents().html())
ul.remove_class("list")
print(ul.parents().html())
print(ul.find(".item-0.active").html())
print(ul.find(".item-0.active").text())
li = doc("ul .item-0.active")

print(doc(".item-0.active").find("a").attr.href)
print(li.attr('class'))
for i in doc("li").items():
    print(i)
print(li.siblings())
print(ul.parents("#tony"))
print(ul.parents())
print(ul.parent())
print(ul.children("#tony"))
print(ul.children())
print(ul.find("li"))
print(doc)
print(type(doc))
print(doc('li'))
print(doc(".item-0"))
print(doc("#tony"))
print(doc("li a"))
'''


