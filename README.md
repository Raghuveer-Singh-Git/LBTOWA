# Insuring the uninsured using XRPL - LBTOWA
Agricultural communities face financial risks and threats to their livelihoods. Our solution aims to reduce financial risk posed by unpredictable weather, providing a safety net for these communities.

The lack of access to quick and reliable insurance for farmers leaves them vulnerable to climate change and its effects. Agricultural Insurance (Weather Futures): This is a form of coverage that protects farmers from financial losses caused by severe weather conditions such as high rainfall, low rainfall, and heatwaves. It provides a safety net for agricultural communities, ensuring sustainable incomes despite unpredictable weather patterns. 
Problems with Current Insurance Models: The current insurance models lack adequate coverage of the unique challenges faced by these communities and businesses. They may need to offer more coverage for the wide range of weather conditions and events that can impact these sectors. There’s a need for more robust and comprehensive insurance solutions that can provide stability and resilience in the face of these challenges.

By creating a simple UI and weather futures trading platform HxH provides the solution to these challenges.

## Our Structure
We will be the central party to issue tokens for our products. The tokens will act as proof of purchase of our products. The tokens can be traded on the open market by the buyer creating "Tradable Insurance". On the settlement date tokens linked to products with a non 0 value can be redimed through us. Bets are a limited loss product and hence no deposit other than the token cost will be required. For all unlimited loss products we will requite buyers to make refundable deposits.

## Our Products

### Futures
* Year to Date (YTD)
  - YTD futues will be based on a index which tracks the difference in YTD weather
* HDD & CDD
  - The concept of Heating Degree Day (HDD) and Cooling Degree Day (CDD) indices originated from observations by engineers who noted that commercial buildings often required heating to maintain an indoor temperature of 70°F when daily mean outdoor temperatures fell below
  - 65°F. Conversely, air conditioning might be needed when temperatures rose significantly above 65°F. The mathematical expressions for HDD and CDD are as follows:
  - HDD = Max(0, 65°F - daily average temperature)
  - CDD = Max(0, daily average temperature - 65°F)
  - For instance, if a day's average maximum and minimum temperature is 35°F, the HDD for that day is 30, and the CDD is 0.
  - The original HDD and CDD futures are based on cumulative values throughout a specific month. For example, an average daily temperature of 45°F corresponds to an HDD of 20 (65°F - 45°F). If the daily average temperature exceeds 65°F, the HDD for that day is zero. A monthly contract is cash settled at the cumulative value of HDDs recorded each day of the month.
  - Consider a month with 31 days, where the average daily temperature is 45°F. The cumulative monthly HDD would be 620 (31 days x 20). The futures contract value is determined by multiplying this figure by $20, resulting in a contract value of $12,400 (=$20 x 620) in this example.
* Direct Index based
  - Direct futures will simply track the underlying rain or temprature index

### Bets
At the start of each month/period equal amounts of ‘above’ and ‘below’ tokens are created with the total price for 1 ‘above’, and 1 ‘below’ token being $1.01 (1 cent of which is our fee). The ‘above’ and ‘below’ tokens are initially priced based on weather forecasts, though the prices change and follow free market/AMM pricing models once trading starts.

At the end of the month/period, when the data is available the tokens evaluate to either $1 or $0 based on the weather conditions. For instance, if the average daily temperature in Singapore is above 30 °C in January 2023 then a 33 °C January 2023 Singapore ‘above’ token will payout $1 to its owner, and a corresponding ‘below’ token would payout $0 to its owner. The tokens will function similarly for average precipitation by region.

## How can our products be used to hedge against unpridictable weathers?

### Futures
Weather-based indices are measures of weather variables that are correlated with farmers’ losses and risks. They can be used to design and implement index insurance, which is a type of crop insurance that pays out when the weather index falls below or above a certain threshold. Index insurance can help farmers to cope with the impacts of climate change, such as droughts, floods, pests, and diseases, by providing them with financial protection and incentives to adopt climate-smart practices.

### Replicating Options - E.g. Reverse Iron Condor
<img src="https://assets-global.website-files.com/5fba23eb8789c3c7fcfb5f31/600704d165d536960eb59357_ia1f9TZOxdYbVWXwcIF9tuX5qMEO5Aw9Lk63He2MY9BL8n8-pcXEE4EiaZv68ha6RjEugqB9SbOCsdUTrB2Qf0rB66c4ZGyTBOdWZckmfsN12Fif4DLQ_pmNNdXiYBoWrrFHqPYb.png" style="width: 400px">
Farmers can experience loss of yield for many scenarios. Lack of precipitation (drought), too much precipitation (floods), too high, or too low temperatures all can cause drops or even total loss of yield. Farmers can hedge against these by buying the corresponding tokens. For instance, a farmer adversely affected by cool temperature and hot temperature may purchase ‘above’ tokens for 30°C while purchasing below tokens for 25°C (Replicating a Reverse Iron Condor). The farmer would then purchase enough tokens such that the value of their lost crop yield is replaced by the payout of the tokens in case of adverse weather. The farmer can further stagger his insurance purchases to fully protect the yield.


For instance, if the farmer has a yield of $500 each January, and loses 10% of that yield for each 10mm decrease in precipitation, with a full yield at 200mm. The farmer will buy the 10%*$500=$50 of the 190mm precipitation ‘below’ tokens, $50 of the 180mm precipitation ‘below’ tokens and so on, allowing him to fully and most effectively insure his farm against a drop in rainfall.

## Future Work
Unfortunately XRPL does not have Smart Contracts integrated on chain yet. While the EVM sidechain is usable for a smart contract implementation, the smart contracts we would need designed would be complicated enough (oracle based-escrow function, token lock-up function, with the contract changing each time the token is traded) that the gas fees would make the insurance project unfeasible.

As a solution, we will continue with our current method, and switch to XRPL hooks for the smart contract functions on layer 1 XRPL when hooks are added to the mainnet. This would allow us to execute the smart contract with lower fees, and allow the entire system to function in a decentralised manner, making it a trustless system, something safer for farmers to adopt.


