# OnePy--构建属于自己的量化回测框架

> 地址：[https://zhuanlan.zhihu.com/p/27730907](https://zhuanlan.zhihu.com/p/27730907)

交易过程中的各个环节，就像是一个一个事件，称为Events，简单来说的话可以分为四个环节（灰色竖线），四种事件（点）。

>> Feed：负责数据读取，产生Market Event。
- Market Event：将数据传递给Strategy模块。
>> Strategy：数据经过交易策略思路，产生交易信号Signal Event。
- Signal Event：将信号信息，如做多做空，手数，执行价格等传递给Portfolio。
>> Portfollio：将信号进行处理，经过风控过滤，产生Order Event。
- Order Event：将交易信息传递给Execution执行。
>> Execution：根据不同broker的手续费多少等，最后完成交易，形成Fill Event。
- Fill Event：完成交易后将信息集合形成交易记录。

流程如下：

读取数据-->处理数据，产生交易信号-->处理交易信号，产生订单-->处理订单，完成交易

借助python的Queue模块，将这一切整合起来。

```
while event_queue_isnt_empty():
    event = get_latest_event_from_queue();
    if event.type == "tick":
        strategy.calculate_trading_signals(event);
    else if event.type == "signal":
        portfolio.handle_signal(event);
    else if event.type == "order":
        portfolio.handle_order(event);
    else if event.type == "fill":
        portfolio.handle_fill(event)
```
结合vnpy中的时间循环方案来看，事件驱动的过程可以为：

- 注册事件处理函数，格式为：{type_:handler};
- 开始监听事件：
  - 传入事件，事件的格式为{type_:data};
  - 根据事件的type_来寻找处理的函数，然后用函数处理data；
- 结束整个过程；

基于以上思路，我们可以得到以下的处理方案：

- 读取数据
  - 可以直接用pandas读取csv文件，用统一的时间戳即可，然后按照时间戳的顺序来提供数据
  - 统一计算交易需要的因子数据
- 处理数据，得到交易信号
  - 根据因子，经过简单处理，或者模型计算后，可以得到交易信号
  - 当然，也可以直接将模型的预测值作为因子数据，将其移到第一步中去
- 根据交易信号进行交易
  - 用一个回测的模块就行了
- 记录交易结果
  - 在交易的过程中，直接完成，和上面一步合并

总体来看，我们已有的框架是可以的，能够快速完成回测，不需要各种复杂的操作。
