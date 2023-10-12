import mplfinance as mpf
import indicator
import updateData
import warnings


def plotStock(target_stock, type, MACD_check, RSI_check ,KD_check, BBAND_check, start, end):
    warnings.filterwarnings('ignore')
    name = updateData.searchStock(target_stock)
    df = updateData.stockData(target_stock, start)
    title = f'{name} {target_stock}'


    # 把綠漲紅跌改成紅漲綠跌
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    style = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, y_on_right=False, edgecolor="black")
    df = indicator.RSI(df, 14)
    df = indicator.BBANDS(df)
    df = indicator.MACD(df)
    df = indicator.KD(df)
    # 畫其中一段時間

    tdf = df.loc[start:end,:]

    """
    panel: 畫在第幾張畫布上
    label: 圖例
    """

    add_plots = []
    panel = 1
    if BBAND_check:
        a = mpf.make_addplot(tdf['upper'], panel=0, label='upper', linestyle='--', width=0.5)
        b = mpf.make_addplot(tdf['middle'], panel=0, label='middle', color='y', linestyle=':', width=0.8)
        c = mpf.make_addplot(tdf['lower'], panel=0, label='lower', linestyle='--', width=0.5)
        add_plots.extend([a, b, c])
    if MACD_check:
        panel += 1
        a = mpf.make_addplot(tdf['MACD'], panel=panel, ylabel='MACD', color='fuchsia', secondary_y=False, label='MACD', width=0.8)
        b = mpf.make_addplot(tdf['MACDsingal'], panel=panel, color='b', secondary_y=False, label='singal', width=0.8)
        c = mpf.make_addplot(tdf['MACDhist'], type='bar', width=0.7, panel=panel, color='dimgray', alpha=1, secondary_y=False)
        add_plots.extend([a,b,c])

    if KD_check:
        panel += 1
        a = mpf.make_addplot(tdf['slowk'], panel=panel, ylabel='KD', label='K', width=0.8)
        b = mpf.make_addplot(tdf['slowd'], panel=panel, label='D', width=0.8)
        add_plots.extend([a,b])

    if RSI_check:
        panel += 1
        add_plots.append(mpf.make_addplot(tdf["RSI"], panel=panel, ylabel="RSI", color="purple", label=f"RSI {tdf['RSI'][-1]:.2f}"))

    """
    figratio: 圖的大小
    figscale: 圖的比例
    volume: 成交量的圖
    mav: 移動平均線(單位天)
    type 可選 candle or line
    """

    fig, axes = mpf.plot(tdf, type=type, addplot=add_plots, figscale=1, figratio=(15,12),
                        style=style, volume=True, returnfig=True)
    # 改字體讓中文可以顯示
    fig.suptitle(title, fontfamily='Microsoft JhengHei')
    # 圖例
    axes[2].set_ylabel("Volume")
    if BBAND_check:
        axes[0].legend(fontsize=10, loc='lower left', frameon=True)
    for i in range(1, panel):
        axes[2*i+2].legend(fontsize=10, loc='lower left', frameon=True)

    fig.savefig(f"{target_stock}.jpg")


