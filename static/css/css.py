16/09/21
上课会讲, 这里简单分类


盒模型相关的 CSS


border
    border-width
    border-style
    border-color

border-top
    border-top-width
    border-top-style
    border-top-color

border-right
    border-right-width
    border-right-style
    border-right-color

border-bottom
    border-bottom-width
    border-bottom-style
    border-bottom-color

border-left
    border-left-width
    border-left-style
    border-left-color



margin
    margin-top
    margin-right
    margin-bottom
    margin-left

padding
    padding-top
    padding-right
    padding-bottom
    padding-left

三种缩写, 分别对应有 4 2 3 个值的时候的解释, padding 同理
margin: top  right  bottom  left
margin: (top/bottom)  (right/left)
margin: top  (right/left)  bottom

border-radius 左上角为 top, 右下角为 bottom






background 相关属性和缩写


background-color: #233;
background-image: url(bg.png);
background-repeat: no-repeat;
background-attachment: fixed; /* 背景图片随滚动轴的移动方式 */
background-position: top right; /* 这个属性的取值非常掏粪但是用得很少, 只在特殊的情况下有用 */

background: #233 url(bg.png) no-repeat top right;





list 属性和缩写


list-style-type: circle;
list-style-position: inside;
list-style-image: url(list.png);

list-style: circle inside url(list.png);





font 设置


font-style: italic;
font-variant: small-caps;
font-weight: bold;
font-size: 20px;
line-height: 1.5em;
font-family: Arial, sans-serif;


font:italic small-caps bold 20px/1.5em Arial, sans-serif;




显示相关的属性

visibility: visible;
            hidden;     /* 不影响子元素 */

overflow: visible;
          hidden;
          scroll;
          auto;




display
position: static | relative | absolute | fixed | sticky
当 position 不为 static 的时候, 元素就是 positioned elements
此时会开启下面 5 个秘密属性
    top
    right
    bottom
    left
    z-index

特殊属性
float
clear

非 inline 元素可以设置盒子尺寸
width
height
min-width
min-height
max-width
max-height




杂七杂八的垃圾

/* 可以叠加效果 */
text-decoration: underline overline line-through blink(这个值已经废弃了);

text-align: left | right | center | justify
vertical-align 偶尔有用
text-transform: none | capitalize | uppercase | lowercase
text-indent: 100px;

纯垃圾属性
unicode-bidi
direction






查文档
搜索 mdn 属性值
