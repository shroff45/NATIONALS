import React from 'react';
export function withErrorRecovery<T>(WrappedComponent: React.ComponentType<T>) {
    return function WithErrorRecovery(props: T & JSX.IntrinsicAttributes) {
        return <WrappedComponent {...props} />;
    }
}
