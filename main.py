"""
Todo
ADX單獨畫或畫ADX和其他一個指標時會閃退
"""


import mplfinance as mpf
import indicator
import updateData
import warnings


def plotStock(target_stock, type, MACD_check, RSI_check ,KD_check, BBAND_check, EMA_check, ATR_check, ADX_check, Volume_check, start, end):
    warnings.filterwarnings('ignore')
    name = updateData.searchStock(target_stock)
    df = updateData.stockData(target_stock, start)
    title = f'{name} {target_stock}'


    # 把綠漲紅跌改成紅漲綠跌
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    style = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, y_on_right=False, edgecolor="black")
    tdf = df.loc[start:end, :]

    """
    panel: 畫在第幾張畫布上
    label: 圖例
    """

    add_plots = []
    if Volume_check:
        panel = 1
    else:
        panel = 0
    if BBAND_check:
        tdf = indicator.BBANDS(tdf)
        a = mpf.make_addplot(tdf['upper'], panel=0, label='upper', linestyle='--', width=0.5)
        b = mpf.make_addplot(tdf['middle'], panel=0, label='middle', color='y', linestyle=':', width=0.8)
        c = mpf.make_addplot(tdf['lower'], panel=0, label='lower', linestyle='--', width=0.5)
        add_plots.extend([a, b, c])
    if MACD_check:
        panel += 1
        tdf = indicator.MACD(tdf)
        a = mpf.make_addplot(tdf['MACD'], panel=panel, ylabel='MACD', color='fuchsia', secondary_y=False, label='MACD', width=0.8)
        b = mpf.make_addplot(tdf['MACDsingal'], panel=panel, color='b', secondary_y=False, label='singal', width=0.8)
        c = mpf.make_addplot(tdf['MACDhist'], type='bar', width=0.7, panel=panel, color='dimgray', alpha=1, secondary_y=False)
        add_plots.extend([a,b,c])

    if KD_check:
        panel += 1
        tdf = indicator.KD(tdf)
        a = mpf.make_addplot(tdf['slowk'], panel=panel, ylabel='KD', label='K', width=0.8)
        b = mpf.make_addplot(tdf['slowd'], panel=panel, label='D', width=0.8)
        add_plots.extend([a,b])

    if RSI_check:
        panel += 1
        tdf = indicator.RSI(tdf, 14)
        add_plots.append(
            mpf.make_addplot(tdf["RSI"], panel=panel, ylabel="RSI", color="purple", label=f"RSI {tdf['RSI'][-1]:.2f}"))

    if ATR_check:
        panel +=1
        tdf = indicator.ATR(tdf)
        add_plots.append(
            mpf.make_addplot(tdf["ATR"], panel=panel, ylabel="ATR", color="green", label=f"ATR {tdf['ATR'][-1]:.2f}"))

    if ADX_check:
        panel +=1
        tdf = indicator.ADX(tdf)
        add_plots.append(
            mpf.make_addplot(tdf["ADX"], panel=panel, ylabel="ADX", color="orange", label=f"ADX {tdf['RSI'][-1]:.2f}"))

    if EMA_check:
        tdf = indicator.EMA(tdf)
        a = mpf.make_addplot(tdf['EMA5'], panel=0, label="5 days", width=0.8)
        b = mpf.make_addplot(tdf['EMA10'], panel=0, label="10 days", width=0.8)
        c = mpf.make_addplot(tdf['EMA20'], panel=0, label="20 days", width=0.8)
        add_plots.extend([a, b, c])

    """
    figratio: 圖的大小
    figscale: 圖的比例
    volume: 成交量的圖
    mav: 移動平均線(單位天)
    type 可選 candle or line
    """

    fig, axes = mpf.plot(tdf, type=type, addplot=add_plots, figscale=1, figratio=(15,12),
                        style=style, volume=Volume_check, returnfig=True)
    # 改字體讓中文可以顯示
    fig.suptitle(title, fontfamily='Microsoft JhengHei')
    # 圖例
    if Volume_check:
        axes[2].set_ylabel("Volume")
        for i in range(1, panel):
            axes[2 * i + 2].legend(fontsize=10, loc='lower left', frameon=True)
    else:
        for i in range(0, panel):
            axes[2 * i + 2].legend(fontsize=10, loc='lower left', frameon=True)
    if BBAND_check:
        axes[0].legend(fontsize=10, loc='lower left', frameon=True)
    for i in range(1, panel):
        axes[2*i+2].legend(fontsize=10, loc='lower left', frameon=True)

    fig.savefig(f"{target_stock}.jpg")


