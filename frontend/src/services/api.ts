import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const api = axios.create({
    baseURL: API_URL,
    headers: {
        "Content-Type": "application/json",
    },
});

export interface TransactionCreate {
    user_id: number;
    from_currency: string;
    to_currency: string;
    amount: number;
}

export interface TransactionRead {
    id: number;
    user_id: number;
    from_currency: string;
    to_currency: string;
    from_value: number;
    to_value: number;
    rate: number;
    timestamp: string;
}

export const convertCurrency = async (data: TransactionCreate) => {
    const response = await api.post<TransactionRead>("/convert", data);
    return response.data;
};

export const getTransactions = async (userId: number) => {
    const response = await api.get<TransactionRead[]>(`/transactions?userId=${userId}`);
    return response.data;
};

export default api;
