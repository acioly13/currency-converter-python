import React, {useState} from "react";
import TransactionList from "./components/TransactionList";
import { convertCurrency } from "./services/api";
import type { TransactionCreate, TransactionRead } from "./services/api";

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
            amount
        };
        try {
            const data = await convertCurrency(payload);
            setResult(data);
        } catch (error) {
            console.error("Conversion error:", error);
        }
    };

    return (
        <div style={{padding: "20px"}}>
            <h1>Currency Converter</h1>

            <div>
                <input type="number" value={amount} onChange={(e) => setAmount(Number(e.target.value))}/>
                <input type="text" value={fromCurrency}
                       onChange={(e) => setFromCurrency(e.target.value.toUpperCase())}/>
                <input type="text" value={toCurrency} onChange={(e) => setToCurrency(e.target.value.toUpperCase())}/>
                <button onClick={handleConvert}>Convert</button>
            </div>

            {result && (
                <div>
                    <h3>Result</h3>
                    <p>
                        {result.from_value} {result.from_currency} → {result.to_value} {result.to_currency} |
                        Rate: {result.rate}
                    </p>
                </div>
            )}

            <TransactionList userId={userId}/>
        </div>
    );
};

export default App;
