import React, { useState, useEffect } from 'react';
import axios from 'axios';

type Props = {
    children: React.ReactNode;
};

export const getProtectedData = async (endpoint) => {
    const response = await axios.get(endpoint, { withCredentials: true });
    return response.data;
};

export const postProtectedData = async (endpoint, body) => {
    const response = await axios.post(endpoint, body, { withCredentials: true });
    return response.data;
};

export const checkAuthorization = async () => {
    try {
        const response = await axios.get(`/auth/check_authorization`, { withCredentials: true });
        return response.data;
    } catch (error) {
        return { authorized: false };
    }
};

export default function WithAuth(props: Props){
    const {children } = props;
    const [isTokenFetchingActive, setTokenFetchingStatus] = useState(true);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        // TODO remake this
        /* const fetchToken = async () => {
            try {
                if (isExpired){
                    removeToken();
                    const access_token = await auth();
                    setToken(access_token);
                    setIsAuthenticated(true);
                    setTokenFetchingStatus(false);
                }
            } catch (err) {
                const msg =
                    err instanceof Error ? err.message : 'Unknown Error: api.get.token';

                // реализуем утилитарное предупреждение для пользователя
                // eslint-disable-next-line no-alert
                alert(
                    `Неудалось загрузить токен доступа. Напишите об этом разработчику, тг - @n1ghtcore194. Ошибка: ${msg}`
                );

                window.location.assign(`/login`);
            }
        };

        if (isTokenFetchingActive) {
            const token = getToken();

            if (token && !isExpired(token.timeStamp)) {
                setIsAuthenticated(true);
                setTokenFetchingStatus(false);
            } else {
                fetchToken();
            }
        }*/
    }, [isTokenFetchingActive]);

    const renderContent = () => {
        return isAuthenticated ? children : null;
    };

    return <div>{isTokenFetchingActive && renderContent()}</div>;
}


