# Tax-Calculator
新个税计算器。【输入】税前收入、五险一金 【输出】新旧两种税率下的应纳税款和税后收入

根据全国人大常委会关于修改个人所得税法的决定，10月1日起，纳税人的工资、薪金所得将适用新的费用减除标准(通常说的“起征点”)，由每月3500元提高到每月5000元，并适用新的个税税率表。

旧税率
![avata](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGGv2iaEaibcQib6P1rqEEOs87Sk6tFMqwu0hQSkBGk6MKb03KxLLRdqhcKDiclOeMqVBkXbM0q4nTAhA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
新税率
![avata](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGGv2iaEaibcQib6P1rqEEOs87taxSjNTCXyVk0FZNicq3TP7MEEmW1B6dvQuYdLRiaK6dvZtE7r0sj5Uw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

实现一个个税计算器：
【输入】税前收入、五险一金
【输出】新旧两种税率下的应纳税款和税后收入

个税计算公式：
应纳税所得额 = 税前收入 - 五险一金 - 起征点
应纳税额 = 应纳税所得额 × 税率 - 速算扣除数

效果演示：
![avata](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGGv2iaEaibcQib6P1rqEEOs87lkKbcDia1bSp2LU5s1G7iabTY5uZQoHXVYkqCyRr7oZ2P6LnzvbwpmPQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
