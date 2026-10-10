import React from 'react';

export function withErrorRecovery<T extends object>(Component: React.ComponentType<T>): React.ComponentType<T> {
  return function WithErrorRecovery(props: T) {
    return React.createElement(Component, props);
  }
}
