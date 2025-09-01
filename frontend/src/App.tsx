import React, {useState} from "react";
import TransactionList from "./components/TransactionList";
import {convertCurrency} from "./services/api";
import type {TransactionCreate, TransactionRead} from "./services/api";

const App: React.FC = () => {
    const [userId] = useState(1);
    const [fromCurrency, setFromCurrency] = useState("USD");
    const [toCurrency, setToCurrency] = useState("BRL");
    const [amount, setAmount] = useState(100);
    const [result, setResult] = useState<TransactionRead | null>(null);

    const handleConvert = async () => {
        const payload: TransactionCreate = {
            user_id: userId,
            from_currency: fromCurrency,
            to_currency: toCurrency,
            amount,
        };
        try {
            const data = await convertCurrency(payload);
            setResult(data);
        } catch (error) {
            console.error("Conversion error:", error);
        }
    };

    return (
        <div className="container">
            <h1>Currency Converter</h1>

            <div className="converter">
                <label htmlFor="amount">Amount:</label>
                <input
                    id="amount"
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(Number(e.target.value))}
                />

                <label htmlFor="from">From:</label>
                <select
                    id="from"
                    value={fromCurrency}
                    onChange={(e) => setFromCurrency(e.target.value)}
                >
                    <option value="BRL">BRL - Brazilian Real</option>
                    <option value="USD">USD - US Dollar</option>
                    <option value="EUR">EUR - Euro</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                </select>

                <label htmlFor="to">To:</label>
                <select
                    id="to"
                    value={toCurrency}
                    onChange={(e) => setToCurrency(e.target.value)}
                >
                    <option value="BRL">BRL - Brazilian Real</option>
                    <option value="USD">USD - US Dollar</option>
                    <option value="EUR">EUR - Euro</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                </select>

                <button onClick={handleConvert}>Convert</button>
            </div>

            {result && (
                <div className="result">
                    <p>
                        {result.from_value.toFixed(2)} {result.from_currency} →{" "}
                        {result.to_value.toFixed(2)} {result.to_currency}
                    </p>
                    <p>Rate: {result.rate.toFixed(2)}</p>
                </div>
            )}

            <div className="transactions">
                <TransactionList userId={userId}/>
            </div>
        </div>
    );
};

export default App;
