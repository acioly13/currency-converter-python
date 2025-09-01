import React, {useEffect, useState} from "react";
import {getTransactions} from "../services/api";
import type {TransactionRead} from "../services/api";

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
            <div className="transactions-list">
                {transactions.map((t) => (
                    <div key={t.id} className="transaction-card">
                        <p>
                            <strong>
                                {t.from_value.toFixed(2)} {t.from_currency}
                            </strong>{" "}
                            → <strong>{t.to_value.toFixed(2)} {t.to_currency}</strong>
                        </p>
                        <p className="rate-date">
                            Rate: {t.rate.toFixed(2)} | {new Date(t.timestamp).toLocaleString()}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TransactionList;
