---
title: "Order Manager"
slug: "wongio-order-manager"
excerpt: "wongio.order-manager@0.12.1"
hidden: true
createdAt: "2022-07-06T19:55:21.269Z"
updatedAt: "2022-07-07T23:09:53.599Z"
---
> Centralizes the requests queue to the Checkout API and manages order form data.

## Warning 🚨

This repository contains **experimental** code for VTEX Checkout and should **not** be used in production.

This code is "experimental" for various reasons:
- Some are not tested as rigorously as the main code.
- Some are tested but not maintained.
- It can suffer from significant changes (breaking changes) without further notice.

**Use it at your own risk!** ☠️

## Usage

```tsx
import { OrderQueueProvider, useOrderQueue, useQueueStatus } from 'vtex.order-manager/OrderQueue'
import { OrderFormProvider, useOrderForm } from 'vtex.order-manager/OrderForm'

const MainComponent: FunctionComponent = () => (
  <OrderQueueProvider>
    <OrderFormProvider>
      <MyComponent />
    </OrderFormProvider>
  </OrderQueueProvider>
)

const MyComponent: FunctionComponent = () => {
  const { enqueue, listen } = useOrderQueue()
  const { orderForm, setOrderForm } = useOrderForm()
  const queueStatusRef = useQueueStatus(listen)
  
  //...
}
```

## `OrderQueue` API

### `useOrderQueue(): OrderQueueContext`

Exposes the API to interact with the order queue. See the items below for more details.

### `enqueue(task: () => Promise, id?: string): CancellablePromise`

> Returned by `useOrderQueue()`

Add a task to the queue of requests to the Checkout API. `task` will be called when it's the first in the queue.

The optional param `id` can be used to duplicate requests. Example:

```ts
const taskA = () => console.log("Task A ran");
enqueue(taskA, "coupon");

// Task A did not run yet and another task with id `coupon` is added to the queue
const taskB = () => console.log("Task B ran");
enqueue(taskB, "coupon");

// Log: 'Task B ran'
// Order Manager will only run taskB and discard taskA.
```

The point of this feature is to avoid making requests that are stale.

Returns a promise that resolves when the task is completed. This promise has a method `.cancel()`. If this function is called, the queue will ignore this task if it hasn't started yet and the promise will immediately reject, returning an object with a property `code` with value `'TASK_CANCELLED'`.

#### Use cases

1. If the user submits a coupon code, the task is scheduled, then changes and type another coupon code, we can avoid making the first request since the second will superseed it.

### `listen(event: QueueStatus, callback: Function): UnsubcribeFunction`

> Returned by `useOrderQueue()`

Once this function is called, the `callback` function will be called whenever the specified `event` is emitted until the returned function is called.

An event is emitted whenever the queue changes its status (see [QueueStatus](#QueueStatus)). For instance, if the queue changes from `QueueStatus.FULFILLED` to `QueueStatus.PENDING`, a `QueueStatus.PENDING` event is emitted.

Returns a function to unsubscribe the callback from the specified event.

#### Use cases

1. Makes it possible to add loaders or disable the Checkout button when there are tasks to resolve.

### `isWaiting(id: string): boolean`

> Returned by `useOrderQueue()`

Returns `true` if there is a task in the queue with the specified `id` that hasn't been run yet, or `false` otherwise.

#### Use cases

1. If you want to enqueue a task but a similar one is already in the queue, you can use this function to determine whether the older one has already been run. In case it hasn't, you can cancel it, merge both tasks and enqueue the merged task.

### `QueueStatus`

An enum that represents the queue states. The possible values are:

- `QueueStatus.PENDING`: There is a task running and there might be other tasks enqueued.
- `QueueStatus.FULFILLED`: The queue is empty and no task is being run.

### `useQueueStatus(listen: ListenFunction): React.MutableRefObject<QueueEvent>`

A helper hook that takes the `listen` function returned by `useOrderQueue` and returns a `ref` object whose `.current` property is a string equal to `Pending` or `Fulfilled` indicating the current queue status.

#### Use cases

1. Makes it possible to perform actions conditioned on the queue status.

#### Example

```ts
const { QueueStatus, useOrderQueue, useQueueStatus } from 'vtex.order-manager/OrderQueue'

const Component: FunctionComponent = () => {
  const { listen } = useOrderQueue()
  const queueStatusRef = useQueueStatus(listen)

  const handleClick = () => {
    if (queueStatusRef.current === QueueStatus.PENDING) {
      console.log('An action was performed while the queue was busy.')
    }
  }
  
  // ...
}
```

#### Notes

- Keep in mind that mutating the `ref` object does not trigger a re-render of the React component. If you want to display content depending on the queue status, consider using states controlled by queue events instead.

## `OrderForm` API

### `useOrderForm(): OrderFormContext`

Exposes the API to interact with the order form. See the items below for more details.

### `loading: boolean`

> Returned by `useOrderForm()`

This flag is set to `true` only when `OrderManager` is loading the order form during render. In order to know whether a task is ongoing, use `listen` instead.

#### Use cases

1. Make it possible to render a loading state when loading a page.

### `orderForm: OrderForm`

> Returned by `useOrderForm()`

Contains data from the order form. Do not modify this directly, use `setOrderForm` instead. In case the order form query fails, an empty order form is returned instead (see [`error`](#error-apolloerror--undefined)).

### `setOrderForm: (newOrderForm: Partial<OrderForm>) => void`

> Returned by `useOrderForm()`

Updates the order form stored in `OrderManager`. This should be called after each mutation to ensure that client data does not get out of sync with server data and that other `OrderManager` consumers can react to this update.

### `error: ApolloError | undefined`

> Returned by `useOrderForm()`

A reference to the `error` object returned by the GraphQL query for the order form.