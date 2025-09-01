import React, {useEffect, useState} from "react";
import { getTransactions } from "../services/api";
import type { TransactionRead } from "../services/api";


interface Props {
    userId: number;
}

const TransactionList: React.FC<Props> = ({userId}) => {
    const [transactions, setTransactions] = useState<TransactionRead[]>([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const data = await getTransactions(userId);
                setTransactions(data);
            } catch (error) {
                console.error("Error fetching transactions:", error);
            }
        };
        fetchTransactions();
    }, [userId]);

    return (
        <div>
            <h2>Transactions</h2>
            <ul>
                {transactions.map((t) => (
                    <li key={t.id}>
                        {t.from_value} {t.from_currency} → {t.to_value} {t.to_currency} |
                        Rate: {t.rate} | {new Date(t.timestamp).toLocaleString()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TransactionList;
