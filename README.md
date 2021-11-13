# Simple Storage using Brownie

## 1. **Pre-requisites**

---

### 1.1. [**Brownie**](https://pypi.org/project/eth-brownie/)

- Install pipx

```
python -m pip install --user pipx
python -m pipx ensurepath
```

- Install Brownie using **pipx**

```
pipx install eth-brownie
```

### 1.2 [**Metamask Account**](https://metamask.io/)

- Add some Test ETH via [Rinkeby Faucet](https://faucet.rinkeby.io/)

### 1.3 [**Infura Account**](https://infura.io/)

- Add a network for Test Rinkeby

## 2. **Brownie Commands**

---

### 1. Initialize Brownie Project

```
brownie init
```

### 2. Compile

```
brownie compile
```

### 3. Run Scripts

```
brownie run .\scripts\deploy.py
```

or

```
brownie run .\scripts\deploy.py --network rinkeby
```

### 4. Accounts

```
brownie accounts
brownie accounts new <account-name>
```

### 5. Run Tests

```
brownie test
brownie test -k <test-name.py>
```

## 3. **Useful Pointers**

---

- Contracts are stored in `contracts` folder
- Scripts are stored in `scripts` folder
- Tests are stored in `tests` folder
