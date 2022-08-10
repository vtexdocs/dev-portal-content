---
title: "Awesome Newsletter"
slug: "gregory-awesome-newsletter"
excerpt: "gregory.awesome-newsletter@0.6.1"
hidden: true
createdAt: "2022-08-05T15:15:31.239Z"
updatedAt: "2022-08-05T15:15:31.239Z"
---
Exports components to make an highly modular and customizable newsletter
## Configuration
You must wrap the Awesome Newsletter© (patent pending) blocks inside the newsletter block, which contains the context provider.

### `awesome-newsletter` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `Entity`      | `string`       | Data entity acronym defined in masterdata         | `NL`        |
| `resetAfterSuccess`      | `boolean`       | If newsletter should be reset its fields after success        | `true`        |

### `awesome-newsletter.email` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `fieldEntity`      | `string`       | Field entity defined in masterdata | `email`        |
| `label`      | `string`       | Text to be render in input label | `undefined`        |
| `placeholder`      | `string`       | Text to be render in input placeholder | `Insira o seu e-mail`        |
| `errorMessage`      | `string`       | Text to be render in case of an invalid input value | `O e-mail inserido parece estar incorreto.`        |

### `awesome-newsletter.name` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `fieldEntity`      | `string`       | Field entity defined in masterdata | `name`        |
| `label`      | `string`       | Text to be render in input label | `undefined`        |
| `placeholder`      | `string`       | Text to be render in input placeholder | `Insira o seu nome`        |
| `errorMessage`      | `string`       | Text to be render in case of an invalid input value | `O valor inserido não é valido.`        |

### `awesome-newsletter.submit` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `label`      | `string`       | Text to be render inside button | `Cadastrar`        |

## Usage example

```json
{
  ...
  
	"awesome-newsletter": {
		"children": ["flex-layout.row#newsletter-fields"],
		"props": {
			"entity": "NL",
			"blockClass": "newsletter"
		}
	},

	"flex-layout.row#newsletter-fields": {
		"children": ["awesome-newsletter.email", "awesome-newsletter.submit"],
		"props": {
			"preventHorizontalStretch": true,
			"blockClass": "newsletter-inputs"
		}
	},
	"awesome-newsletter.email": {
		"props": {
			"label": "E-mail",
			"placeholder": "Insira o seu e-mail "
		}
	},
	"awesome-newsletter.submit": {
		"props": {
			"label": "Cadastrar"
		}
	}
}
```

## Contributors
- Evailson `Eva`
- Rafael `Brown`
- Jonathan `Mineiro`